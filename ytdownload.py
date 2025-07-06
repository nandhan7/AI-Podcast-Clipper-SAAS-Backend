from pytubefix import YouTube
from pytubefix.cli import on_progress

url1="https://www.youtube.com/watch?v=SOG0GmKts_I"
url2="https://www.youtube.com/watch?v=-vMgbJ6WqN4&ab_channel=AToastToLifePodcast"
url3="https://www.youtube.com/watch?v=eK71EN3P78U&ab_channel=RawTalksWithVK"

yt=YouTube(url3,on_progress_callback=on_progress)
print(yt.title)

ys=yt.streams.get_highest_resolution()
ys.download()
