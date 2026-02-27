
from tkinter import *

from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from sys import exc_info
def lcheck(link):
    if "https://" in link:
        return True
    else:
        return False

def clean(link):
    sep = ['&si=', '?si=']
    for x in sep:
        link = link.split(x, 1)[0]
    return link





colors=["#191923",'#213851',"#f5f5f5","#f61067","#3777ff","#00c49a"]
# black, darkblue, white, magenta, blue, mint

window = Tk()
window.title("KittyTunnel V2.0")
window.geometry('600x200')

window.configure(bg=colors[0])


lbl = Label(window, text="Built on PyTubeFix under MIT licensing https://github.com/juanbindez/pytubefix" ,bg=colors[1], fg=colors[2])
lbl.grid(column=1, row=0, sticky=W)
lbl1 = Label(window, text="Made by Mowrious" ,bg=colors[0], fg=colors[2], justify="left")
lbl1.grid(column=1, row=1, sticky=W)

lbl2 = Label(window, text=" Link : ",bg=colors[0], fg=colors[2])
lbl2.grid(column=0, row=2, sticky=W)

txt = Entry(window,width=71 ,bg=colors[1], fg=colors[2])
txt.grid(column=1, row=2, sticky=N)


# video downloads
def clicked1():
    a = lcheck(txt.get())
    if a:
        downl = clean(txt.get())
        try:
            yt = YouTube(downl, on_progress_callback=on_progress)
            yt = yt.streams.get_highest_resolution()
            res = downl +"\n"+yt.title
            lbl3.configure(text=res)
            yt.download('./video')
        except Exception as e:
            res = "ERROR: ", e
        else:
            res = res + "\n\nDownload finished!    saved to ./video folder."
    else:
        res =  "\n\nInvalid link!"
    lbl3.configure(text= res)
#audio download
def clicked2():
    a = lcheck(txt.get())
    if a:
        downl = clean(txt.get())
        try:
            yt = YouTube(downl, on_progress_callback=on_progress)
            yt = yt.streams.get_audio_only()
            res = downl +"\n"+yt.title
            lbl3.configure(text=res)
            yt.download('./audio')
        except Exception as e:
            res = "ERROR: ", e
        else:
            res = res + "\n\nDownload finished!    saved to ./audio folder."
    else:
        res = "\n\nInvalid link!"
    lbl3.configure(text=res)

def clicked3():
    res = "canceled"
    lbl3.configure(text= res)

btn = Button(window, text="Video", command=clicked1, width=8 ,bg=colors[4], fg=colors[0])
btn.grid(column=1, row=3, sticky=W)
btn1 = Button(window, text="Audio", command=clicked2, width=8 ,bg=colors[5], fg=colors[0])
btn1.grid(column=1, row=3, sticky=W, padx=80)
btn2 = Button(window, text="Cancel", command=clicked3, width=8 ,bg=colors[3], fg=colors[2])
btn2.grid(column=1, row=3, sticky=E)

lbl3 = Label(window, text="",bg=colors[0], fg=colors[2], justify="left")
lbl3.grid(column=1, row=4, sticky=W)
window.mainloop()

