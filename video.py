from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam
from moviepy.editor import *
from pytube import YouTube

class Video:
    def __init__(self,url) -> None:
        self.url=url
        
    def mp3_download(self):
        """télécharge le fichier mp3 de la vidéo"""
        file_path = os.path.realpath(__file__)
        realpath=file_path[0:len(file_path)-8]
        realpath=realpath.replace("\\",'/')
        video = YouTube(self.url)
        print(f'Downloading video')
        video.streams.filter(file_extension='mp4').first().download(filename=f'{realpath}audio.mp4')
        print('Successful Download')
        print(f'Now converting to MP3')
        mp4_file=f'{realpath}audio.mp4'
        mp3_file=f'{realpath}audio.mp3'
        videoclip=VideoFileClip(mp4_file)
        audioclip=videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        print('Successful Conversion')
        os.remove(f"{realpath}audio.mp4")

        
        
    
    def clean_workspace(self):
        file_path = os.path.realpath(__file__)
        realpath=file_path[0:len(file_path)-8]
        realpath=realpath.replace("\\",'/')
        if os.path.isfile(f"{realpath}audio.mp3"):
            os.remove(f"{realpath}audio.mp3")
        

        
