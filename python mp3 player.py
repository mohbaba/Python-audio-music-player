from pydub import AudioSegment
from pydub.playback import play
import glob
import os


playlist = "C:/Users/hp/Desktop/gbedu/"
song_title = "01 Afterglow.m4a"
song = os.path.join(playlist,song_title)
new_song = AudioSegment.from_file(song)
playlist_list = os.listdir(playlist)
print(playlist)
# play(new_song)
clean_audio = []
# for files in playlist:
#     clean_audio.append()
    # files_list = [AudioSegment.from_file(playlist) ]
    