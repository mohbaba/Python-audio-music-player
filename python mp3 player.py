from pydub import AudioSegment
from pydub.playback import play
import glob
import os


playlist = "C:/Users/hp/Desktop/gbedu/"
song_title = "01 Afterglow.m4a"
# song = os.path.join(playlist,song_title)
# new_song = AudioSegment.from_file(song)
playlist_list = os.listdir(playlist)

print(playlist_list)
# play(new_song)
clean_audio = []
os.chdir(playlist)
for files in playlist_list:
    exported_files = AudioSegment.from_file(files)
    song_start = exported_files[:10*1000]
    play(song_start)
    