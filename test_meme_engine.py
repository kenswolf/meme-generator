"""Manages unit tests of the Meme Engine"""

import unittest
from meme_engine import MemeEngine


class TestMemeEngine(unittest.TestCase):
    """Manages the unit tests of the Meme Engine"""

    def test_meme_engine_completes(self):
        """Verify that the meme engine can complete a call"""

        me = MemeEngine("./test_memes")
        out_path = me.make_meme(
            "./_data/photos/dog/xander_1.jpg", "Hello!", "Dickens", 400
        )
        print(out_path)
        self.assertEqual(len(out_path) > 0, True)


if __name__ == "__main__":
    unittest.main()
