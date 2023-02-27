from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
print("Title: " + str(yt.title) + " ")
print("Views: " + str(yt.views) + " ")
print("Author: " + str(yt.author) + " ")
print("Publish date: " + str(yt.publish_date) + " ")
print("Is age restricted: " + str(yt.age_restricted) + "")
print("Channel URL is: " + str(yt.channel_url) + "")
print("Streams: " + str(yt.streams) + "")


yd = yt.streams.get_highest_resolution()
yd.download('/path/to/save')
