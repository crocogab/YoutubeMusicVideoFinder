from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam
from moviepy.editor import *
from pytube import YouTube



class Audio:
    """Nouvelle classe audio qui traite mtn le mp3"""
    def __init__(self,path):
        self.path=path
    
    def cut_mp3(self,i=0):
        """coupe l'audio par segment de 1 minute et produit 1 nom différent par fichier"""
        file_path = self.path
        realpath=file_path[0:len(file_path)-9]
        realpath=realpath.replace("\\",'/')
        sound=AudioSegment.from_file(self.path)
        duree=len(sound) # duree de laudio 
        for i in range(int((len(sound)/1000)/60)): #cree un fichier tout les 1 min
            second_half = sound[i*1000*60:((i+1)*1000*60)]
            second_half.export(f"{realpath}/audio_final/audio{i}.mp3", format="mp3")
    
    def cut_mp3_extrait(self,audio_directory):
        """Coupe des extraits de 5s (à la fin de la musique)"""
        entries = os.listdir(audio_directory)
        
        for i in entries :
           if  os.path.isdir(f'{audio_directory}/{i}')==True:
               pass
           else:
             print(f'{i} processing | Output : /extract/ \n')
             song=AudioSegment.from_file(f'{audio_directory}/{i}')
             first_5_seconds=song[:5000]
             last_5_seconds = song[-5000:]
             last_5_seconds.export(f"{audio_directory}/extract/{i}", format="mp3")
             first_5_seconds.export(f"{audio_directory}/extract/first_{i}", format="mp3")
    
    def clean_workspace(self):
        print("Cleaning of the workspace in progress to avoid any bugs :)")
        file_path = self.path
        realpath=file_path[0:len(file_path)-9]
        realpath=realpath.replace("\\",'/')
        
        dir1=f'{realpath}audio_final'
        dir2=f'{realpath}audio_final/extract/'
        
        for f in os.listdir(dir1) :
           if os.path.isfile(f'{dir1}/{f}'):
               os.remove(os.path.join(dir1, f))
           else:
               pass
        for f in os.listdir(dir2):
           os.remove(os.path.join(dir2, f))
    