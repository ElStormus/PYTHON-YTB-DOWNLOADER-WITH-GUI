#!python3
#coding=utf-8

from importlib.resources import path
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import tkinter
import pytube
import sys
from PIL import ImageTk, Image
import webbrowser
from pytube import YouTube
#from urllib.request import urlopen
#from pytube import Playlist
#from urllib import *
#import urllib
#from urllib.request import urlretrieve


root = tk.Tk()

# Tkinter window settings
root.geometry("800x500")
Tk_Width = 800
Tk_Height = 500
x_Left = int(root.winfo_screenwidth()/2 - Tk_Width / 2)
y_Top = int(root.winfo_screenheight()/ - Tk_Height / 2)
root.geometry("+{}+{}".format(x_Left, y_Top))

root.iconbitmap('img/Youtube_Thumb.ico')
root.resizable(False, False)
root.grid_rowconfigure(0, weight = 0)
root.grid_columnconfigure(0, weight = 0)
root.title("YTB DOWNLOADER (BETA)")

# For downloading from Youtube
def Youtube():
    #labelDWLD = Label(root, text='Download in progress, please wait').place(x=310, y=260)
    global URL
    string = URL.get()
    yt = pytube.YouTube(string, on_progress_callback = progress_func)
    labelTitle = Label(root, text = yt.title).place(x = 350, y = 320)
    yt.streams.filter(progressive=True, file_extension = 'mp4').get_highest_resolution().download(path)
    #labelDWLD.place_forget()
    labelDWLDDONE = Label(root, text = 'Download complete').place(x = 335, y = 260)
    labelVid = Label(root, text = 'Your video :').place(x = 280, y = 320)
    
    #Thumbnails = yt.thumbnail_url
    #urllib.request.urlretrieve(Thumbnails, "./img/Thmb.png")
    #imgThmb = ImageTk.PhotoImage(Image.open("./img/Thmb.png"))
    #panelThmb = tk.Label(root, image=imgThmb)
    #panelThmb.place(x=0, y=0)

# For the progress bar (experimental)
def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    labelPG = Label(root, text="\r[{}{}] ".format('=' * done, ' ' * (50-done))).place(x = 200, y = 280)
    #sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
    #sys.stdout.flush()

# Open Github's link
def link():
    webbrowser.open_new("https://github.com/ElStormus/-GUI-YTB_DOWNLOADER")


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

    # The user link input
    URL = Entry(root, width = 80)
    URL.focus_set()
    URL.place(x = 150, y = 180)
    ttk.Button(root, text = "Download", width = 20, command = Youtube).place(x = 325, y = 230)

    # The button for Github's link
    github_link = PhotoImage(file ="img/github.png")
    Button(root, text = 'Click Me !', image = github_link, command = link).place(x = 5, y = 460)

    labelVers = Label(root, text = "By PESSON Victor  BETA | 0.1").place(x = 635, y = 470)

    messagebox.showwarning("Informations", "Warning, downloading copyrighted video or audio from Youtube is illegal. \n \n I am not responsible for your use of this tool. \n \n /!\ This tool is still under development and may be unstable. In case of bug, please let me know on GitHub. ")

    # Choosing where to save files
    path = filedialog.askdirectory(title = "Select where you want to save your files")
     
    root.mainloop()