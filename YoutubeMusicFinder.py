import video 
import audio 
from pydub import AudioSegment
import os
import os.path
from ShazamAPI import Shazam
import sys
import optparse
from optparse import OptionParser
from moviepy.editor import *
from pytube import YouTube

timecode=[]


actual_folder = os.path.realpath(__file__)
actual_folder = actual_folder[0:len(actual_folder)-21]
actual_folder = actual_folder.replace("\\",'/')

audio_final_full_dir=f'{actual_folder}audio_final'
audio_directory=f'{audio_final_full_dir}/extract'

parser = OptionParser(usage='usage: %prog [options] arguments')
parser.add_option('-u', '--url', 
                        dest='URL',
                        help='The url of the target Youtube vidéo')
(url, args) = parser.parse_args()
if not url.URL:   
    parser.error('You have to enter a URL')
url=url.URL

video1=video.Video(url)
video1.clean_workspace()
video1.mp3_download()

video1_audio=audio.Audio(f"{actual_folder}audio.mp3")
video1_audio.clean_workspace()
video1_audio.cut_mp3()
video1_audio.cut_mp3_extrait(audio_final_full_dir)

def find_song(file_path,time):
    mp3_file_content_to_recognize = open(file_path, 'rb').read()
    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    reponse=next(recognize_generator)[1]
    a={time+1:(reponse['track']['title'])}
    return(a)


entries = os.listdir(audio_directory)
liste_musique = {}  


for i,j in enumerate(entries):
  try: 
      nom=find_song(f'{audio_directory}/{j}',i)
      print(f'Processing {j}')
      liste_musique.update(nom)

  except KeyError:
      print(f'Processing {j}')
    
    
    

liste_finale={}
for i in liste_musique:
    if liste_musique[i] in liste_finale:
        pass
    else:
        liste_finale[i]=liste_musique[i]

temp = {val: key for key, val in liste_finale.items()}
liste_finale = {val: key for key, val in temp.items()}

if all(value == 0 for value in liste_finale.values()):
    liste_finale={'No music found in this video':''}
for key in liste_finale:
    print(f'Timecode : {key} min | {liste_finale[key]}')


