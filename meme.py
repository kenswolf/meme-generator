""" Generate meme files """

import os
import random

from argparse import ArgumentParser

from ingestor import Ingestor
from meme_engine import MemeEngine
from quote_model import QuoteModel


def get_quotes() -> list:
    """get all quotes including one that will be used to make meme"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    return quotes


def get_quote(body: str = None, author: str = None) -> QuoteModel:
    """Get quote that will be used to make meme.
    In some cases, this produces misattributed quotes,
    but that is the requirement of this project.
    The rubric very clearly states about the option cmd line arguements ...
    'If any argument is not defined, a random selection is used.'"""

    if body is not None and author is not None:
        quote = QuoteModel(body, author)
    else:
        quotes = get_quotes()
        quote = random.choice(quotes)
        if body is not None:
            quote.body = body
        elif author is not None:
            quote.author = author

    return quote


def get_images(image_folder_path: str) -> list:
    """get filepath of each of the images"""

    # imgs = []
    # for root, _, files in os.walk(image_folder_path):
    #   imgs = [os.path.join(root, name) for name in files]
    # return imgs
    image_file_names = os.listdir(image_folder_path)
    list_of_image_file_paths = [
        os.path.join(image_folder_path, filename) for filename in image_file_names
    ]
    list_of_image_file_paths = [
        ifp for ifp in list_of_image_file_paths if os.path.isfile(ifp)
    ]

    return list_of_image_file_paths


def get_image(path: str) -> str:
    """get filepath of image that will be used to make meme"""

    if path is None:
        imgs = get_images("./_data/photos/dog/")
        img = random.choice(imgs)
    else:
        img = path

    return img


def generate_meme(path: str = None, body: str = None, author: str = None) -> str:
    """Generate a meme, given an path to an image, and a quote"""

    img = None
    quote = None

    img = get_image(path)
    quote = get_quote(body, author)
    meme = MemeEngine("./memes")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = ArgumentParser(description="parsing arguements for meme generation")

    parser.add_argument(
        "-p",
        "--path",
        nargs="?",
        help="An optional path parameter. The value is a path to an image file.",
    )
    parser.add_argument(
        "-b",
        "--body",
        nargs="?",
        help="An optional body parameter. The value is a quote body to add to the image.",
    )
    parser.add_argument(
        "-a",
        "--author",
        nargs="?",
        help="An optional author parameter. The value is a quote author to add to the image",
    )
    args = parser.parse_args()

    path_to_meme = generate_meme(args.path, args.body, args.author)
    print(path_to_meme)
