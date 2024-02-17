""" PDF file-type specific concrete ingestor class """

import os
from typing import List
import subprocess
from quote_model import QuoteModel
from ingestor_interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """PDF file-type specific concrete ingestor class"""

    @classmethod
    def _extract_text_to_temp_file(cls, input_path: str, output_path: str) -> int:
        """Extract text from pdf file into a temp file that is easy to work with"""

        rtn = 0
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", input_path, output_path],
                check=True,
                text=True,
                capture_output=True,
            )
            if result.returncode != 0:
                rtn = result.returncode
                print(f"pdftotext failed with return code {result.returncode}.")
                print(f"Error message: {result.stderr}")

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            rtn = 99

        return rtn

    @classmethod
    def _read_and_parse_temp_file(
        cls, output_path: str, quotes: List[QuoteModel]
    ) -> None:
        """Read the temp text file and parse contents into list of QuoteModel instances"""

        try:
            with open(output_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "\f":
                        vals = line.split("-")
                        body = vals[0].strip().strip('"')
                        author = vals[1].strip()
                        quote = QuoteModel(body, author)
                        quotes.append(quote)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except FileNotFoundError:
            print(f"Error: File '{output_path}' not found.")
        except PermissionError:
            print("Permission to read temp file was denied.")
        except IOError as e:
            print(f"I/O error during temp file read: {e}")

    @classmethod
    def _remove_temp_file(cls, output_path: str) -> None:
        """Remove temp file, ie cleanup"""
        try:
            os.remove(output_path)
        except FileNotFoundError:
            print(f"Error: File '{output_path}' not found.")
        except PermissionError:
            print("Permission to remove temp file was denied.")
        except IOError as e:
            print(f"I/O error during temp file removal: {e}")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parsing a pdf file"""

        quotes = []

        output_path = path + "_temp.txt"
        rtn = cls._extract_text_to_temp_file(path, output_path)
        if rtn == 0:
            cls._read_and_parse_temp_file(output_path, quotes)
            cls._remove_temp_file(output_path)

        return quotes
