import pygame


class MusicPlayer:
    def play(self, song_path):
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

        while True:
            command = input('> ')
            if command == 'pause':
                pygame.mixer.music.pause()
            elif command == 'stop':
                pygame.mixer.music.fadeout(200)
            elif command == 'unpause':
                pygame.mixer.music.unpause()
            elif command == 'exit':
                break

        pygame.mixer.quit()

MusicPlayer().p('/home/betrakiss/Music/Five Finger Death Punch - Battle Born.mp3')
