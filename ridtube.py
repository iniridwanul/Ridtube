from pytube import YouTube
import banner
import os

#Show Logo
os.system("clear")
banner.showlogo()

#Start Processing
select_resolution = input("High/Low: ")
select_resolution = select_resolution.lower()
if select_resolution == "high":
    video_url = input("Enter Video Link: ")
    print("Download has started")
    ridtube = YouTube(video_url)
    ridtube = ridtube.streams.get_highest_resolution()
    ridtube.download()
    print("Download Complete")
elif select_resolution == "low":
    video_url = input("Enter Video Link: ")
    print("Download has started")
    ridtube = YouTube(video_url)
    ridtube = ridtube.streams.first()
    ridtube.download()
    print("Download Complete")
else:
    print("Please try again")