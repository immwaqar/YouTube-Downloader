## Import Libraries

from tkinter import *  # Tkinter is a GUI library
from pytube import YouTube # used to download video from youtube

## Creating Display Windows
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root,text= 'Youtube Video Downloader', font='ariel 20 bold').pack()


## Create Field to Enter Link
link = StringVar()
Label(root, text= 'Paste Link Here:', font= 'ariel 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable= link).place(x=32, y=90)


## Creating Function to Start Downloading
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text= 'Downloaded', font='ariel 15').place(x=180, y=210)
    

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()