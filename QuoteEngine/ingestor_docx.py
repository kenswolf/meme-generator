""" DOCX file-type specific concrete ingestor class """

from typing import List

from docx import Document

from quote_model import QuoteModel
from ingestor_interface import IngestorInterface

class DocxIngestor(IngestorInterface):
    """DOCX file-type specific concrete ingestor class"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parsing a docx file"""

        quotes = []

        try:

            doc = Document(path)
            for line in doc.paragraphs:
                if len(line.text) > 0:
                    vals = line.text.split("-")
                    quote = QuoteModel(vals[0].strip(), vals[1].strip())
                    quotes.append(quote)

        except FileNotFoundError:
            print("DOCX file was not found.")
        except PermissionError:
            print("Permission to read docx file was denied.")
        except IOError as e:
            print(f"I/O error during docx file read: {e}")
        except UnicodeDecodeError as e:
            print(f"Unicode decoding problem with docx file: {e}")

        return quotes
