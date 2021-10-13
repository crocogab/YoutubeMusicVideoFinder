import video 
import audio 
import pafy
from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam

actual_folder = os.path.realpath(__file__)
actual_folder = actual_folder[0:len(actual_folder)-21]
actual_folder = actual_folder.replace("\\",'/')

audio_final_full_dir=f'{actual_folder}audio_final'
audio_directory=f'{audio_final_full_dir}/extract'

url='https://www.youtube.com/watch?v=6ZpdIvsifV4'

video1=video.Video(url)
video1.clean_workspace()
video1.mp3_download()

video1_audio=audio.Audio(f"{actual_folder}audio.mp3")
video1_audio.clean_workspace()
video1_audio.cut_mp3()
video1_audio.cut_mp3_extrait(audio_final_full_dir)

def find_song(file_path):
    
    mp3_file_content_to_recognize = open(file_path, 'rb').read()
    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    reponse=next(recognize_generator)[1]
    a=(reponse['track']['title'])
    return(a)


entries = os.listdir(audio_directory)
liste_musique = []  


for i in entries:
  try: 
      nom=find_song(f'{audio_directory}/{i}')
      print(f'Traitement en cours de {i}')
      liste_musique.append(nom)

  except KeyError:
      print(f'Traitement en cours de {i}')
    
    
    

liste_finale=list(set(liste_musique))
if len(liste_finale)==0:
    liste_finale.append('Aucune musique trouvée dans cette vidéo')
for i in liste_finale:
  print(f'Musique trouvée : {i}')


