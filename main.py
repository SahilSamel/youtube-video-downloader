from tkinter.constants import BOTTOM
from tkinter.font import names
from pytube import YouTube
import tkinter
from tkinter import messagebox
import os

def downloader():
    link = givelink_entry.get()
    path = download_path.get()
    try:
        yt = YouTube(str(link))
    except:
        messagebox.showerror("Error", "There was a problem!")
    else:
        vid = yt.streams.get_highest_resolution()
        vid.download(path)
        os.startfile(path)
        return messagebox.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {path}{yt.title}")

win = tkinter.Tk()

win.geometry("450x300")
win.title("YouTube Video Downloader")

frame = tkinter.LabelFrame(win)
frame.grid(row=0, column=0, padx=70, pady=90)

#Labels
givelink = tkinter.Label(frame, text="Enter video Link")
givelink.grid(row=0, column=1)

savepath = tkinter.Label(frame, text="Where to save")
savepath.grid(row=3, column=1)


#Entries
givelink_entry = tkinter.Entry(frame, width=50)
givelink_entry.grid(row=1, columnspan=3)

download_path = tkinter.Entry(frame, width=50)
download_path.grid(row=4, columnspan=3)

#button
download_btn = tkinter.Button(frame, text="Download Video",width=15, command=downloader)
download_btn.grid(row=7, columnspan=3)


win.mainloop()
