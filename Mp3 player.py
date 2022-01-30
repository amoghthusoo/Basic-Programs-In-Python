# Program to play Mp3/WAV file
# VLC MediaPlayer and python-vlc module should be installed.

import vlc

class Mp3_Player:

    def __init__(self, path):
        self.path = path
        self.song_handler = None

    def play(self):

        self.song_handler = vlc.MediaPlayer(self.path)
        self.song_handler.play()

def main():

    obj = Mp3_Player("monody.mp3")
    obj.play()
    print('Press Enter to abort!')
    input()

if __name__ == '__main__':
    main()
