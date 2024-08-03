import tkinter as tk
from tkinter import filedialog
import yt_dlp
import os


def download_mp3():
    url = url_entry.get()
    if not url:
        status_label.config(text="URL cannot be empty", fg="red")
        return

    try:
        download_folder = filedialog.askdirectory()
        if not download_folder:
            status_label.config(text="Download  canceled", fg="red")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'ffmpeg_location': '/path/to/ffmpeg/bin',  # Replace with the path to ffmpeg on your system
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.config(text="Download complete! File saved to: " + download_folder, fg="green")
    except Exception as e:
        status_label.config(text="Error: " + str(e), fg="red")


root = tk.Tk()
root.title("YouTube to MP3 Converter")

tk.Label(root, text="Insert the URL of the video:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download MP3", command=download_mp3)
download_button.pack(pady=20)

status_label = tk.Label(root, text="", wraplength=400)
status_label.pack(pady=5)

root.mainloop()
