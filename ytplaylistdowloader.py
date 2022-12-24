
from pytube import Playlist

link = 'https://www.youtube.com/playlist?list=PLXtgXP89Tyn-aRmrnfNsio7LvG1BWy9eb'
link1= input('input playlist link youtube')
yt_playlist = Playlist(link1)
print(yt_playlist)

for video in yt_playlist.videos:
    print("video downloading...")
    video.streams.get_highest_resolution().download()
    print("Video Downloaded: ", video.title)

print("\nAll videos are downloaded.")