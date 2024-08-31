from pytube import YouTube
from yt_dlp import YoutubeDL


link = input("Enter youtube video")
yt = YouTube(link)

# To print title
print("Title :", yt.title)
# To get number of views
print("Views :", yt.views)
# To get the length of video
print("Duration :", yt.length)
# To get description
print("Description :", yt.description)
# To get ratings
print("Ratings :", yt.rating)


download_option = input("Do you want to download this video? (yes/no): ").lower()

if download_option == "yes":
    url = link
    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([url])
        print("Download completed.")
else:
    print("Download aborted.")