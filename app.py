""" Manage meme process """

import random
from flask import Flask, render_template, request
import meme_temp_file_util as fu
from meme_engine import MemeEngine
import meme as mm


app = Flask(__name__)

meme = MemeEngine("./static")

IMAGE_FOLDER = "./_data/photos/dog/"


def setup():
    """Load all resources"""
    _quotes = mm.get_quotes()
    _imgs = mm.get_images(IMAGE_FOLDER)
    return _quotes, _imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""
    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]

    path_to_saved_image = fu.save_url_image(image_url, meme.output_folder)
    path_to_meme = meme.make_meme(path_to_saved_image, body, author)
    fu.remove_temp_file(path_to_saved_image)

    return render_template("meme.html", path=path_to_meme)


if __name__ == "__main__":
    app.run()
