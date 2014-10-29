import json
from song import Song


class Playlist:
    MAX_BITRATE = 320

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

    def list_songs(self):
        for i, song in enumerate(self.songs):
            print('[{0}] {1} - {2}'.format(i, song.artist, song.title))

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
            if each.bitrate < self.MAX_BITRATE:
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

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def save(self, file_name):
        burnable = open(file_name, 'w')
        burnable.write(self.to_JSON())

        burnable.close()

    @staticmethod
    def load(file_name):
        readable = open(file_name, 'r')
        data = json.load(readable)

        result = Playlist(data['name'])
        for song in data['songs']:
            result.add_song(Song(song['title'], song['artist'], song['album'],
                                 song['rating'], song['length'], song['bitrate']))

        return result
