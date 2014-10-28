import os
import datetime
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from playlist import Playlist
from song import Song


class MusicCrawler:
    _NULL_RATING = 0

    def __init__(self, directory):
        self.directory = directory

    def get_file_names(self):
        self.files = os.listdir(self.directory)

    def get_tag(self, mpeg3, tag):
        try:
            result = mpeg3[tag][0]
        except BaseException:
            return 'Unknown'

        return result

    def generate_playlist(self):
        self.get_file_names()
        result = Playlist('Playlist 1')

        for each in self.files:
            audio = MP3('{0}/{1}'.format(self.directory, each), ID3=EasyID3)
            result.add_song(Song(audio['title'][0], audio['artist'][0], audio['album'][0],
                                 self._NULL_RATING,
                                 str(datetime.timedelta(seconds=audio.info.length)),
                                 audio.info.bitrate))

        return result

crawler = MusicCrawler('/home/betrakiss/Music')
play = crawler.generate_playlist()

play.save('test.txt')
