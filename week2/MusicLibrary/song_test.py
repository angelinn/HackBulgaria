import unittest
from song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("BeatBox", "PsychoFrog", "BB 2015", 4, 190, 320)

    def test_init(self):
        self.assertEqual("BeatBox", self.test_song.title)
        self.assertEqual("PsychoFrog", self.test_song.artist)
        self.assertEqual("BB 2015", self.test_song.album)
        self.assertEqual(4, self.test_song.rating)
        self.assertEqual(190, self.test_song.length)
        self.assertEqual(320, self.test_song.bitrate)

    def test_rate_invalid_value(self):
        with self.assertRaises(ValueError):
            self.test_song.rate(10)

    def test_rate_with_valid_value(self):
        self.test_song.rate(4)
        self.assertEqual(4, self.test_song.rating)

if __name__ == '__main__':
    unittest.main()
