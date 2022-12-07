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
# print(playlist_list)

def playlist_player():
    for file in playlist_list:
        # exported_files = AudioSegment.from_file(file)
        mixer.music.load(file)
        mixer.music.play()
        # query = input("Press 'p' to pause")
        # if query == 'p':
        #     mixer.music.pause()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    
    # os.chdir(playlist)
    # for files in playlist_list:
        # exported_files = AudioSegment.from_file(files)
        # song_start = exported_files[:10*1000]
        # play(song_start)


# while True:
    
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
    
#     if query == 'p':

#         # Pausing the music
#         mixer.music.pause()     
#     elif query == 'r':

#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':

#         # Stop the mixer
#         mixer.music.stop()
#         break
        

def play_song():
    # this function plays the selected song from the song library or playlist
    file = '01 - Starboy (feat. Daft Punk).mp3'
    mixer.music.load(file)
    mixer.music.play()
    # while mixer.music.get_busy():
    # According to the pygame documentation mixer.music.get_busy() returns True if the music is playing
    while True:
        query = input("Press 'p' to pause \n")
        if query == 'p':
            mixer.music.pause()
        else:
            print('type in p to pause \n')
        # while mixer.music.pause():
        #     query = input("Press 'p' to pause")
        #     if query == 'r':
        #         mixer.music.unpause()
            
            
     
play_song()
def pause_song():
    
    while playlist_player():
        query = input("Press 'p' to pause")
        if query == 'p':
            mixer.music.pause()
                   


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