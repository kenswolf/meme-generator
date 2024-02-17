"""Manages unit tests of the IngestorInterface parent class"""

import unittest
from ingestor_interface import IngestorInterface


class TestIngestorInterface(unittest.TestCase):
    """Unit Test the IngestorInterface parent function can-ingest"""

    def test_can_ingest_abc(self):
        """verify filename with unsupported suffix fails can_ingest check"""
        result = IngestorInterface.can_ingest("./dog/foo.abc")
        self.assertEqual(result, False)

    def test_can_ingest_no_suffix(self):
        """verify filename with no suffix fails can_ingest check"""
        result = IngestorInterface.can_ingest("./foo")
        self.assertEqual(result, False)

    def test_can_ingest_pdf(self):
        """verify filename with pdf suffix passes can_ingest check"""
        result = IngestorInterface.can_ingest("./dog/foo.pdf")
        self.assertEqual(result, True)

    def test_can_ingest_txt(self):
        """verify filename with txt suffix passes can_ingest check"""
        result = IngestorInterface.can_ingest("./dog/cat/foo.txt")
        self.assertEqual(result, True)

    def test_can_ingest_csv(self):
        """verify filename with csv suffix passes can_ingest check"""
        result = IngestorInterface.can_ingest("./foo.csv")
        self.assertEqual(result, True)

    def test_can_ingest_docx(self):
        """verify filename with docx suffix passes can_ingest check"""
        result = IngestorInterface.can_ingest("foo.docx")
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
