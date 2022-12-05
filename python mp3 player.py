from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer
import pygame
import os

# pygame.init()
mixer.init()
playlist = "C:/Users/hp/Desktop/gbedu/"
playlist_list = os.listdir(playlist)
os.chdir(playlist)
print(playlist_list)
# play(new_song)
# clean_audio = []
def playlist_player():
    for file in playlist_list:
        # exported_files = AudioSegment.from_file(file)
        mixer.music.load(file)
        mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    # os.chdir(playlist)
    # for files in playlist_list:
        # exported_files = AudioSegment.from_file(files)
        # song_start = exported_files[:10*1000]
        # play(song_start)
playlist_player()
def play_song():
    # this function plays the selected song from the song library or playlist
    pass 

def pause_song():
    pass

def play_next_song():
    # if the next button is pressed,stop the current playing song and then play the next song  
    pass

def play_prev_song():
    pass

def repeat():
    # this repeats the current song until its unpressed
    pass

def repeat_playlist():
    # this function repeats the playlist until its unpressed
    pass