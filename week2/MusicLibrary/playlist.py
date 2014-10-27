import json


class Playlist:
    _MAX_BITRATE = 320

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_title):
        i = 0
        while i < len(self.songs):
            if self.songs[i].title == song_title:
                del self.songs[i]
                i -= 1

            i += 1

    def total_length(self):
        total = 0
        for each in self.songs:
            total += each.length

        return total

    def remove_disrated(self, rating):
        if rating < 0 or rating > 5:
            raise ValueError

        for each in self.songs:
            if each.rating < rating:
                self.remove_song(each.title)

    def remove_bad_quality(self):
        for each in self.songs:
            if each.bitrate < self._MAX_BITRATE:
                self.remove_song(each.title)

    def show_artists(self):
        artists = []

        for each in self.songs:
            if each.artist not in artists:
                artists.append(each.artist)

        return artists

    def __str__(self):
        result = ''
        for each in self.songs:
            result += str(each) + '\n'

        return result

    def save(self, file_name):
        burnable = open(file_name, 'w')
        for each in self.songs:
            burnable.write(json.dumps(each.__dict__))

        burnable.close()

