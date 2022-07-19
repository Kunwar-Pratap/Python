from pytube import YouTube

myLink = input("Enter your link for Download: ")
print("Downloading start...keep patience...")

YouTube(myLink).streams.first().download()
print("Your video downloaded successfully")
