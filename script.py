from pytube import YouTube
from yt_dlp import YoutubeDL


def download_youtube_video(link):
    yt = YouTube(link)

    print("Title :", yt.title)
    print("Views :", yt.views)
    print("Duration :", yt.length)
    print("Description :", yt.description)
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

x = "yes"
while x == "yes":
    link = input("Enter youtube video link :")
    download_youtube_video(link)
    x = input("Do you want to download another video? (yes/no): ").lower()
    if x != "yes":
        print("Thank you for using the Youtube Downloader!")