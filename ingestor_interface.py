""" Abstract interface/parent-class for all ingestor classes """

from typing import List
from abc import ABC
from quote_model import QuoteModel

class IngestorInterface(ABC):

    """ Abstract interface/parent-class for fall ingestor classes """

    types = ['csv', 'docx', 'pdf', 'txt']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """" Check if file type supported"""
        suffix = path.split('.')[-1]
        return suffix in cls.types

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ parse implemented in file type specific concrete classes"""
