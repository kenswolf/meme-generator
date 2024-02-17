"""Manages unit tests of the Meme generation controller code, ie code in meme.py"""

import unittest
import meme
from quote_model import QuoteModel


class TestMeme(unittest.TestCase):
    """Manages the unit tests of the Meme generation controller code"""

    def test_meme_can_load_quotes(self):
        """Verify that the meme code can load quotes from various files"""

        quotes = meme.get_quotes()
        self.assertEqual(len(quotes) == 11, True)

    def test_meme_can_load_quote(self):
        """Verify that the meme code can load a random quote from loaded quotes"""

        quote = meme.get_quote()
        self.assertEqual(isinstance(quote, QuoteModel), True)

    def test_meme_can_load_requested_image(self):
        """Verify that the meme code can load a requested image"""

        path = "./_data/photos/dog/xander_1.jpg"
        new_path = meme.get_image(path)
        self.assertEqual(path == new_path, True)

    def test_meme_can_load_random_image(self):
        """Verify that the meme code can load a random image"""

        img = meme.get_image(None)
        self.assertEqual(len(img) > 0, True)

    def get_data_to_test_meme_can_generate_meme(self):
        """Get data that is used in multiple tests of meme generation"""

        path = "./_data/photos/dog/xander_1.jpg"
        body = "Hello!"
        author = "Dickens"

        return (path, body, author)

    def test_meme_can_generate_meme_when_given_path_body_author(self):
        """Test meme generation with values for path, body, and author"""

        path, body, author = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(path, body, author)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_path_body(self):
        """Test meme generation with a path value and a body value"""

        path, body, _ = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(path, body)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_path_author(self):
        """Test meme generation with a path value and an author value"""

        path, _, author = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(path, None, author)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_body_author(self):
        """Test meme generation with a body value and an author value"""

        _, body, author = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(None, body, author)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_path(self):
        """Test meme generation with just a path value"""

        path, _, _ = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(path)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_author(self):
        """Test meme generation with just an author value"""

        _, _, author = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(None, None, author)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_body(self):
        """Test meme generation with just a body value"""

        _, body, _ = self.get_data_to_test_meme_can_generate_meme()

        try:
            new_path = meme.generate_meme(None, body, None)
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)

    def test_meme_can_generate_meme_when_given_nothing(self):
        """Test meme generation with just a body value"""

        try:
            new_path = meme.generate_meme()
        except ValueError:
            new_path = ""

        self.assertEqual(len(new_path) > 0, True)


if __name__ == "__main__":
    unittest.main()
