"""Manages unit tests of the file-type specific ingestors"""

import unittest
from quote_model import QuoteModel
from ingestor import Ingestor


class TestIngestor(unittest.TestCase):
    """Unit tests the file-type specific ingestors"""

    def test_parse_csv(self):
        """test that a pdf file can be parsed"""
        results = Ingestor.parse("./_data/DogQuotes/DogQuotesCSV.csv")
        self.assertEqual(isinstance(results[0], QuoteModel), True)


if __name__ == "__main__":
    unittest.main()
