#iport youtube library for downloading videos
import pytube
#prompt the youtube video url
url = input("enter youtube video url: ")
#Path can also be used
#uncomment the line
#path = input("Enter path of the storage: ")

#specify the path of the storage
path = "D:"

#magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)