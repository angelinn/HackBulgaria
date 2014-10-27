import unittest
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist('Pro Playlist')
        self.song = Song("BeatBox", "PsychoFrog", "BB 2015", 4, 190, 320)

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertIn(self.song, self.playlist.songs)

    def test_remove_song(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song)

        self.playlist.remove_song(self.song.title)
        self.assertEqual(self.playlist.songs, [])

    def test_total_length(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song)

        self.assertEqual(self.song.length + self.song.length, self.playlist.total_length())

    def test_remove_disrated(self):
        self.playlist.add_song(self.song)
        self.playlist.remove_disrated(5)
        self.assertEqual([], self.playlist.songs)

    def test_remove_disrated_with_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.playlist.remove_disrated(-1)

    def test_remove_bad_quality(self):
        self.playlist.add_song(self.song)
        bad_bit_song = Song("d", "R", "A", 4, 40, 256)
        self.playlist.add_song(bad_bit_song)
        self.playlist.remove_bad_quality()

        self.assertEqual([self.song], self.playlist.songs)

    def test_show_artists(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song)
        self.playlist.add_song(Song("Other Song", "Other Artist", "Album", 5, 180, 320))

        self.assertEqual(["PsychoFrog", "Other Artist"], self.playlist.show_artists())
        #print(self.playlist)
        self.playlist.save('test_playlist.txt')

    #def test_saving(self):
        self.playlist.save('test_playlist.txt')


if __name__ == '__main__':
    unittest.main()
