from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer
import pygame
import os

# pygame.init()

playlist = "C:/Users/hp/Desktop/gbedu/"
playlist_list = os.listdir(playlist)
os.chdir(playlist)
index = 0
print(playlist_list)
print(playlist_list.index('01 Drake - Tuscan Leather.mp3'))
# file = '01 - Starboy (feat. Daft Punk).mp3'
# mixer.music.load(file)
# mixer.music.play()



def playlist_player():
    for file in playlist_list:
        mixer.music.load(file)
        mixer.music.play()
        # query = input("Press 'p' to pause")
        # if query == 'p':
        #     mixer.music.pause()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            pause_song()
    
    # os.chdir(playlist)
    # for files in playlist_list:
        # exported_files = AudioSegment.from_file(files)
        # song_start = exported_files[:10*1000]
        # play(song_start)

        

def play_song():
    # this function plays the selected song from the song library or playlist
    mixer.init()
    file = '01 - Starboy (feat. Daft Punk).mp3'
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            pause_song()
    # while mixer.music.get_busy():
    # According to the pygame documentation mixer.music.get_busy() returns True if the music is playing , but get_busy() does not do exactly what the pygame document says: pause() and unpause() does not change the return value of get_busy().
        
    # while True:
    #     query = input("Press 'p' to pause, 'r' to resume and 'e' to exit \n")
    #     if query == 'p':
    #         mixer.music.pause()
            
            
    #     elif query == 'r':
    #         mixer.music.unpause()
            
                
    #     elif query == 'e':
    #         mixer.music.stop()
            
                
playlist_player()
# play_song()
def pause_song():
    while True:
        query = input("Press 'p' to pause, 'r' to resume and 'e' to exit 'n' to next  \n")
        if query == 'p':
            mixer.music.pause()
        elif query == 'r':
            mixer.music.unpause()
        elif query == 'e':
            mixer.music.stop()
        elif query == 'n':
            global index
            index += 1
            mixer.music.load(playlist_list[index])
            mixer.music.play()
                
            
# play_song()



def play_next_song():
    # if the next button is pressed,stop the current playing song and then play the next song  
    global index
    index += 1
    mixer.music.load(playlist_list[index])
    mixer.music.play()
    
    pass

def play_prev_song():
    pass

def repeat():
    # this repeats the current song until its unpressed
    pass

def repeat_playlist():
    # this function repeats the playlist until its unpressed
    pass

# if __name__ == '__main__':
#     a = Thread(target = play_song)
#     b = Thread(target = pause_song)
    
#     b.start()
#     a.start()