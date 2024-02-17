""" CSV file-type specific concrete ingestor class """

from typing import List
import pandas as pd

from quote_model import QuoteModel
from ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """CSV file-type specific concrete ingestor class"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parsing a csv file"""

        quotes = []

        df = pd.read_csv(path)
        for row in df.index:
            body = df["body"][row]
            author = df["author"][row]
            quote = QuoteModel(body, author)
            quotes.append(quote)

        return quotes

    @classmethod
    def parse_old_but_works(cls, path: str) -> List[QuoteModel]:
        """parsing a csv file"""

        quotes = []

        try:
            with open(path, "r", encoding="utf-8") as f:
                f.readline()
                lines = f.readlines()
                for line in lines:
                    vals = line.split(",")
                    quote = QuoteModel(vals[0].strip(), vals[1].strip())
                    quotes.append(quote)

        except FileNotFoundError:
            print("CSV file was not found.")
        except PermissionError:
            print("Permission to read csv file was denied.")
        except IOError as e:
            print(f"I/O error during csv file read: {e}")
        except UnicodeDecodeError as e:
            print(f"Unicode decoding problem with csv file: {e}")

        return quotes
