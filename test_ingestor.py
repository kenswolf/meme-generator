"""Manages unit tests of the file-type specific ingestors"""

import unittest
from quote_model import QuoteModel
from ingestor import Ingestor


class TestIngestor(unittest.TestCase):
    """Unit tests the file-type specific ingestors"""

    def test_ingest_txt(self):
        """test that a txt file can be ingested"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesTXT.txt")
        self.assertEqual(len(result) > 0, True)

    def test_parse_txt(self):
        """test that a txt file can be parsed"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesTXT.txt")
        self.assertEqual(isinstance(result[0], QuoteModel), True)

    def test_ingest_csv(self):
        """test that a csv file can be ingested"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesCSV.csv")
        self.assertEqual(len(result) > 0, True)

    def test_parse_csv(self):
        """test that a csv file can be parsed"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesCSV.csv")
        self.assertEqual(isinstance(result[0], QuoteModel), True)

    def test_ingest_docx(self):
        """test that a docx file can be ingested"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesDOCX.docx")
        self.assertEqual(len(result) > 0, True)

    def test_parse_docx(self):
        """test that a docx file can be parsed"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesDOCX.docx")
        self.assertEqual(isinstance(result[0], QuoteModel), True)

    def test_ingest_pdf(self):
        """test that a pdf file can be ingested"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesPDF.pdf")
        self.assertEqual(len(result) > 0, True)

    def test_parse_pdf(self):
        """test that a pdf file can be parsed"""
        result = Ingestor.parse("./_data/DogQuotes/DogQuotesPDF.pdf")
        self.assertEqual(isinstance(result[0], QuoteModel), True)


if __name__ == "__main__":
    unittest.main()
