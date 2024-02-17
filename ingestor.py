"""Manage parsing of any supported file type"""

from typing import List
from quote_model import QuoteModel
from ingestor_interface import IngestorInterface

from QuoteEngine import TextIngestor
from QuoteEngine import CSVIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import DocxIngestor

class Ingestor(IngestorInterface):
    """Ingestor is a controller class that delegates 
    parsing to file type specific concrete classes"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse image file using appropriate file type specific ingestor"""
        if cls.can_ingest(path):
            suffix = path.split(".")[-1].lower()
            if suffix == "txt":
                return TextIngestor.parse(path)
            elif suffix == "csv":
                return CSVIngestor.parse(path)
            elif suffix == "pdf":
                return PDFIngestor.parse(path)
            elif suffix == "docx":
                return DocxIngestor.parse(path)
        else:
            return []
