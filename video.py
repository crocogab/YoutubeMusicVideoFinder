import pafy
from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam


class Video:
    def __init__(self,url) -> None:
        self.url=url
        
    def mp3_download(self):
        """télécharge le fichier mp3 de la vidéo"""
        video = pafy.new(self.url)
        print(f'Téléchargement en cours de {video.title} de {video.author} | {video.duration}')
        bestaudio = video.getbestaudio()
        bestaudio.download("audio.mp3")
        file_path = os.path.realpath(__file__)
        realpath=file_path[0:len(file_path)-8]
        realpath=realpath.replace("\\",'/')
        print(realpath)
        
        
