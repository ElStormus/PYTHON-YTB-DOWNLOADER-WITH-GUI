#!python3
#coding=utf-8

from importlib.resources import path
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import tkinter
import pytube
import sys
from PIL import ImageTk, Image, ImageDraw
import webbrowser
from pytube import YouTube
import os, os.path
import time

root = tk.Tk()

# Tkinter window settings
root.geometry("800x500")
Tk_Width = 800
Tk_Height = 500
x_Left = int(root.winfo_screenwidth()/2 - Tk_Width / 2)
y_Top = int(root.winfo_screenheight()/ - Tk_Height / 2)
root.geometry("+{}+{}".format(x_Left, y_Top))

root.iconbitmap('img/icon.ico')
root.resizable(False, False)
root.grid_rowconfigure(0, weight = 0)
root.grid_columnconfigure(0, weight = 0)
root.title("YTB DOWNLOADER (BETA)")


# For downloading from Youtube in MP4
def YoutubeMP4():


    panel3 = tk.Label(root, image = imgContainer)
    panel3.place(x = 155, y = 270)
    global URL
    string = URL.get()
    yt = pytube.YouTube(string)
    yt.streams.filter(progressive = True, file_extension = 'mp4').get_highest_resolution().download(path)
    views = yt.views
    viewsConvert = str(views)
    length = time.strftime("%H:%M:%S", time.gmtime(yt.length))
    lengthConvert = str(length)
    labelDWLDDONE = Label(root, text = 'Download complete').place(x = 335, y = 262)
    labelVid = Label(root, text = 'Your downloaded video :').place(x = 170, y = 290)
    labelTitle = Label(root, text = yt.title).place(x = 210, y = 320)
    labelAuthor = Label(root, text = 'By ' + yt.author).place(x = 330, y = 357)
    labelViews = Label(root, text = viewsConvert + ' views').place (x = 330, y = 375)
    labelLength = Label(root, text = 'Duration : ' + lengthConvert).place (x = 330, y = 392)

def YoutubeMP3():

    panel2 = tk.Label(root, image = imgContainer)
    panel2.place(x = 155, y = 270)
    global URL
    string = URL.get()
    yt = pytube.YouTube(string)
    title = yt.title
    test = yt.streams.filter(only_audio=True).get_audio_only().download(path)
    file_title = title + ".mp4"
    base, ext = os.path.splitext(test)
    new_file = base + '.mp3'
    os.rename(test, new_file)
    views = yt.views
    viewsConvert = str(views)
    length = time.strftime("%H:%M:%S", time.gmtime(yt.length))
    lengthConvert = str(length)
    labelDWLDDONE = Label(root, text = 'Download complete').place(x = 335, y = 262)
    labelVid = Label(root, text = 'Your downloaded video :').place(x = 170, y = 290)
    labelTitle = Label(root, text = title).place(x = 210, y = 320)
    labelAuthor = Label(root, text = 'By ' + yt.author).place(x = 330, y = 357)
    labelViews = Label(root, text = viewsConvert + ' views').place(x = 330, y= 375)
    labelLength = Label(root, text = 'Duration : ' + lengthConvert).place(x = 330, y = 392)

def CmbSelect():

    select = listsFormatsCombo.get()
    if select == "MP4":
        YoutubeMP4()
    else:
        YoutubeMP3()

def OpenDirectory():

    os.startfile(path)

# Open Github's link
def link():

    webbrowser.open_new("https://github.com/ElStormus/YOUTUBE-DOWNLOADER-WITH-GUI-AND-EXE")

def AskPath():

    global path
    del path
    path = filedialog.askdirectory(title = "Select where you want to save your files")

if __name__ == "__main__":

    # Choose format (non fonctionnal for the moment)
    listsFormats = ["MP4", "MP3"]
    listsFormatsCombo = ttk.Combobox(root, values = listsFormats)
    listsFormatsCombo['state'] = 'readonly'
    listsFormatsCombo.current(0)
    listsFormatsCombo.place(x = 660, y = 179, relwidth = 0.07)

    # For the logo
    img = ImageTk.PhotoImage(Image.open("img/Logo_main.png"))
    panel = tk.Label(root, image = img)
    panel.place(x = 320, y = 60)

    imgContainer = ImageTk.PhotoImage(Image.open("img/video_container2.png"))
    panel = tk.Label(root, image = imgContainer)
    panel.place(x = 155, y = 270)

    # The user link input
    URL = Entry(root, width = 80)
    URL.focus_set()
    URL.place(x = 150, y = 180)
    ttk.Button(root, text = "Download", width = 20, command = CmbSelect).place(x = 325, y = 230)

    # The button for Github's link
    github_link = PhotoImage(file = "img/github.png")
    Button(root, text = 'Github', image = github_link, command = link).place(x = 5, y = 460)

    open_folder = PhotoImage(file = "img/folder_icon.png")
    Button(root, text = 'Open Folder', image = open_folder, command = OpenDirectory).place(x = 50, y = 460)

    ask_path = PhotoImage(file = "img/path2.png")
    Button(root, text = 'Ask Path', image = ask_path, command = AskPath).place(x = 95, y = 460)

    labelVers = Label(root, text = "By PESSON Victor  BETA | 0.2").place(x = 635, y = 470)

    messagebox.showwarning("Informations", "Warning, downloading copyrighted video or audio from Youtube is illegal. \n \n I am not responsible for your use of this tool. \n \n /!\ This tool is still under development and may be unstable. In case of bug, please let me know on GitHub.")

    # Choosing where to save files
    path = filedialog.askdirectory(title = "Select where you want to save your files")

    root.mainloop()