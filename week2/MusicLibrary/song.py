import datetime
import math


class Song:
    MAX_RATING = 5
    MIN_RATING = 0

    def __init__(self, file_name, title, artist, album, rating, length, bitrate):
        self.file_name = file_name
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length

        bitrate_length = math.log10(bitrate) + 1

        if bitrate_length > 3:
            self.bitrate = int(bitrate / 1000)

    def rate(self, rating):
        if rating < self.MIN_RATING or rating > self.MAX_RATING:
            raise ValueError

        self.rating = rating

    def __str__(self):
        #sec = datetime.timedelta(seconds=int(self.length))

        return '{0} {1} - {2}'.format(self.artist, self.title, self.length)
