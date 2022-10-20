#!python3
#coding=utf-8

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from pytube import YouTube
from pytube import Playlist
import pytube

root= tk.Tk()

root.geometry("800x500")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)
root.title("YTB DOWNLOADER (BETA)")



def Youtube():
    global URL
    string= URL.get()
    label2 = Label(root, text=string).grid(row=1,column=2)
    yt = pytube.YouTube(string)
    yt.title
    yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution().download()



if __name__ == "__main__":
    
    img = PhotoImage(file="img/Logo_main.jpg")
    panel = tk.Label(root, image=img)
    panel.grid(row=0, column=0, sticky=NW)

    label = Label(root, text="").grid(row=1, column=2)
    URL = Entry(root, width=80)
    URL.focus_set()
    URL.grid(row=1, column=2, sticky=E)
    ttk.Button(root, text= "Download",width= 20, command=Youtube).grid(row=2, column=2)
    
    
    root.mainloop()