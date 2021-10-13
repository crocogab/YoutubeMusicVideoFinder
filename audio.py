import pafy
from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam



class Audio:
    """Nouvelle classe audio qui traite mtn le mp3"""
    def __init__(self,path):
        self.path=path
    
    def cut_mp3(self,i=0):
        """coupe l'audio par segment de 1 minute et produit 1 nom différent par fichier"""
        sound=AudioSegment.from_file(self.path)
        duree=len(sound) # duree de laudio 
        for i in range(int((len(sound)/1000)/60)): #cree un fichier tout les 1 min
            second_half = sound[i*1000*60:((i+1)*1000*60)]
            second_half.export(f"C:/Users/croco/Documents/GitHub/YoutubeMusicFinder/audio_final/audio{i}.mp3", format="mp3")
    
    def cut_mp3_extrait(self,audio_directory):
        """Coupe des extraits de 5s (à la fin de la musique)"""
        entries = os.listdir(audio_directory)
        
        for i in entries :
           if  os.path.isdir(f'{audio_directory}/{i}')==True:
               pass
           else:
             print(f'{audio_directory}/{i} traitement en cours | Output : {audio_directory}/extract/')
             song=AudioSegment.from_file(f'{audio_directory}/{i}')
             last_5_seconds = song[-5000:]
             last_5_seconds.export(f"{audio_directory}/extract/{i}", format="mp3")
    