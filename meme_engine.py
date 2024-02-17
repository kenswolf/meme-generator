""" The Meme Engine Class is responsible for manipulating and drawing text onto images """

import random
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests
import meme_temp_file_util as fu


class MemeEngine:
    """Manipulating images and drawing text onto them"""

    def __init__(self, output_folder: str):
        self.output_folder = output_folder
        folder_path = Path(output_folder)
        if not folder_path.exists():
            folder_path.mkdir(parents=True)

    # this is a pure function so it could have been a class method
    def resize(self, image: Image, width: int) -> Image:
        """Resize image proportionally to provided width"""
        image_width, image_height = image.size
        scaling_ratio = width / image_width
        scaled_height = int(image_height * scaling_ratio)
        resized_image = image.resize((width, scaled_height))
        return resized_image

    def text_will_fit(
        self,
        draw: ImageDraw,
        text_position: tuple,
        msg: str,
        text_font: ImageFont,
        image_width: int,
        image_height: int,
    ) -> bool:
        """Determine if the text will fit on the image"""
        text_box_size = draw.textbbox(text_position, msg, font=text_font)
        return text_box_size[2] < image_width and text_box_size[3] < image_height

    def shift_to_fit(
        self,
        draw: ImageDraw,
        text_position: tuple,
        msg: str,
        text_font: ImageFont,
        image_width: int,
        image_height: int,
    ) -> bool:
        """Move the text starting location in order to make it fit on the image"""
        x, y = text_position
        text_box_size = draw.textbbox(text_position, msg, font=text_font)
        x_prime = x - text_box_size[2] + image_width - 10
        y_prime = y - text_box_size[3] + image_height - 10
        return (x_prime, y_prime)

    def get_text_font_size_and_placement(
        self, draw: ImageDraw, msg: str, image_width: int, image_height: int
    ) -> tuple:
        """Find random location and font size such that the text will fit on the image"""

        x = random.randint(5, image_width // 2)
        y = random.randint(5, image_height - 40)
        text_position = (x, y)

        shift = True
        for font_size in range(35, 10, -5):
            text_font = ImageFont.truetype("font/ShadeBlue-2OozX.ttf", font_size)
            if self.text_will_fit(
                draw, text_position, msg, text_font, image_width, image_height
            ):
                shift = False
                break
        if shift:
            text_position = self.shift_to_fit(
                draw,
                text_position,
                msg,
                text_font,
                image_width,
                image_height,
            )

        return text_position, text_font

    def add_text(self, image: Image, body: str, author: str) -> None:
        """Overlay image with provided text"""

        msg = f"{body} -{author}"
        text_color = (255, 255, 255)  # white
        image_width, image_height = image.size
        draw = ImageDraw.Draw(image)
        text_position, text_font = self.get_text_font_size_and_placement(
            draw, msg, image_width, image_height
        )
        draw.text(text_position, msg, fill=text_color, font=text_font)

    def make_meme(
        self, image_path: str, body: str, author: str, width: int = 500
    ) -> str:
        """Make a meme from an image and provided text"""

        print("making meme from this ...", image_path, body, author)

        new_image_path = None

        try:
            if image_path[:5].lower() == "http":
                url = image_path
                response = requests.get(url, timeout=15)
                image = Image.open(BytesIO(response.content))
            else:
                image = Image.open(image_path)

            resized_image = self.resize(image, width)
            self.add_text(resized_image, body, author)
            new_image_path = fu.save_temp_file(
                resized_image, image_path, self.output_folder
            )
        except FileNotFoundError:
            print("File was not found.")
        except PermissionError:
            print("Permission to read file was denied.")
        except IOError as e:
            print(f"I/O error during file read: {e}")

        return new_image_path
