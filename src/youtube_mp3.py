#!/usr/bin/env python

from __future__ import unicode_literals
import youtube_dl
import sys

URL = sys.argv[1]


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        #'preferredcodec': 'mp3',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])
