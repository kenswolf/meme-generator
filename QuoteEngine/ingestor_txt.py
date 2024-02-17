""" TXT file-type specific concrete ingestor class """

from typing import List

from quote_model import QuoteModel
from ingestor_interface import IngestorInterface

class TextIngestor(IngestorInterface):
    """TXT file-type specific concrete ingestor class"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parsing a txt file"""

        quotes = []

        try:

            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    vals = line.split("-")
                    quote = QuoteModel(vals[0].strip(), vals[1].strip())
                    quotes.append(quote)

        except FileNotFoundError:
            print("TXT file was not found.")
        except PermissionError:
            print("Permission to read txt file was denied.")
        except IOError as e:
            print(f"I/O error during txt file read: {e}")
        except UnicodeDecodeError as e:
            print(f"Unicode decoding problem with txt file: {e}")

        return quotes
