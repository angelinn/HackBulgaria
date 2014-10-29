import pygame
from playlist import Playlist
from music_crawler import MusicCrawler


class MusicPlayer:
    _UNKNOWN_COMMAND = 'Unknown command!'
    _ERROR_MESSAGE = 'Something went terribly wrong ..'
    _MAX_SONGS_REACHED = 'No more songs to play.'
    _MIN_SONGS_REACHED = 'No more songs to rewind.'
    _PROMPT_FOR_PLAYLIST = 'Enter a playlist name > '
    _PROMPT_FOR_DIRECTORY = 'Enter directory for the music to be imported > '

    def __init__(self):
        self.playlist = Playlist(input(self._PROMPT_FOR_PLAYLIST))
        self.directory = input(self._PROMPT_FOR_DIRECTORY)
        self.current_song = -1
        pygame.mixer.init()

    def add_dir(self):
        crawler = MusicCrawler(self.directory)
        self.playlist = crawler.generate_playlist()

    def play(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def make_full_path(self, song_path):
        return self.directory + song_path

    def print_now_playing(self):
        print('Now Playing: {0}'.format(str(self.playlist.songs[self.current_song])))

    def go(self):
        self.add_dir()

        while True:
            try:
                command = input('> ')
                if command == 'list songs':
                    self.playlist.list_songs()

                elif command == 'pause':
                    pygame.mixer.music.pause()

                elif command == 'stop':
                    pygame.mixer.music.fadeout(200)

                elif command == 'unpause':
                    pygame.mixer.music.unpause()

                elif command == 'next':
                    if self.current_song >= len(self.playlist.songs) - 1:
                        print(self._MAX_SONGS_REACHED)

                    else:
                        self.current_song += 1
                        self.print_now_playing()
                        self.play(self.make_full_path(self.playlist.songs[self.current_song].file_name))

                elif command == 'previous':
                    if self.current_song <= 0:
                        print(self._MIN_SONGS_REACHED)

                    else:
                        self.current_song -= 1
                        self.print_now_playing()
                        self.play(self.make_full_path(self.playlist.songs[self.current_song].file_name))

                elif command == 'play':
                    self.current_song = 0 if -1 else self.current_song
                    self.print_now_playing()
                    self.play(self.directory + self.playlist.songs[self.current_song].file_name)

                elif command == 'exit':
                    break

                else:
                    print(self._UNKNOWN_COMMAND)

            except Exception:
                print(self._ERROR_MESSAGE)

        pygame.mixer.quit()


def main():
    MusicPlayer().go()

if __name__ == '__main__':
    main()
