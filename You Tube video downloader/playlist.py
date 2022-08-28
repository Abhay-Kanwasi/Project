# download youtube playlist

from pytube import Playlist
playlist_data = Playlist("https://www.youtube.com/watch?v=E43yJPLI9Wk&list=PLVBKjEIdL9buA0Ulh6QsnVCuwoh3KS__S")

print(f'Downloading : {playlist_data.title}')
for video in playlist_data.videos:
    video.streams.get_highest_resolution().download()