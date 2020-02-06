from __future__ import unicode_literals
import youtube_dl
import os


def get_mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '50',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    for entry in os.scandir('.'):
        if entry.is_file():
            if entry.name.endswith(".flac"):
                if os.path.exists('audio.flac'):
                    os.remove("audio.flac")
                try:
                    os.rename(entry.name, "audio.flac")
                except:
                    continue

    print('uploading')
    os.system(r"C:\Programming\Projects\Python\YHack\upload.bat")
    print("done")


if __name__ == '__main__':
    get_mp3('https://www.youtube.com/watch?v=4WEQtgnBu0I')

