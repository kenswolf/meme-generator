""" PDF file-type specific concrete ingestor class """

import os
from random import randint
from pathlib import Path
from urllib.parse import urlparse
from io import BytesIO
import requests
from PIL import Image


def remove_temp_file(temp_filepath: str) -> None:
    """Remove temp file"""
    try:
        os.remove(temp_filepath)
    except FileNotFoundError:
        print(f"Error: File '{temp_filepath}' not found.")
    except PermissionError:
        print("Permission to remove temp file was denied.")
    except IOError as e:
        print(f"I/O error during temp file removal: {e}")


def get_filename_for_temp_file(perm_image_filepath: str) -> str:
    """Get filename to use for the temp file"""

    random_digits = str(randint(10**5, 10**6 - 1))
    filename = Path(perm_image_filepath)
    new_output_file_name = f"{filename.stem}_{random_digits}{filename.suffix}"
    return new_output_file_name


def get_filepath_for_temp_file(perm_image_filepath: str, target_folder: str) -> str:
    """Get filepath to use for the temp file"""

    new_output_file_name = get_filename_for_temp_file(perm_image_filepath)
    output_folder = Path(target_folder)
    filepath_for_temp_file = str(output_folder.joinpath(new_output_file_name))

    return filepath_for_temp_file


def save_temp_file(image: Image, perm_image_filepath: str, target_folder: str) -> str:
    """Save image to temp file"""
    filepath_for_temp_file = get_filepath_for_temp_file(
        perm_image_filepath, target_folder
    )
    image.save(filepath_for_temp_file)
    return filepath_for_temp_file


def get_url_image_filename(url: str) -> str:
    """get image filename from url"""
    parsed_url = urlparse(url)
    image_filename = os.path.basename(parsed_url.path)
    return image_filename


def save_url_image(url: str, target_folder: str) -> str:
    """save image from url to local file"""
    path_to_saved_image = ""
    try:
        response = requests.get(url, timeout=15)
        image = Image.open(BytesIO(response.content))
        image_filename = get_url_image_filename(url)
        path_to_saved_image = save_temp_file(image, image_filename, target_folder)
    except FileNotFoundError:
        print("File was not found.")
    except PermissionError:
        print("Permission to read file was denied.")
    except IOError as e:
        print(f"I/O error during file read: {e}")

    return path_to_saved_image
