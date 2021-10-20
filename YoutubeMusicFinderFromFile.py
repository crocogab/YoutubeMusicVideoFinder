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



def main():
    actual_folder = os.path.realpath(__file__)
    actual_folder = actual_folder[0:len(actual_folder)-29] # u have to change 29 if u change name of the file 
    actual_folder = actual_folder.replace("\\",'/')

    audio_final_full_dir=f'{actual_folder}audio_final'
    audio_directory=f'{audio_final_full_dir}/extract'

    parser = OptionParser(usage='usage: %prog -f audio.mp3')
    parser.add_option('-f', '--file', 
                            dest='FILE',
                            help='Your mp3 file ')
                            
    (options, args) = parser.parse_args()
    if not options.FILE:   
        parser.error('You have to give an mp3 file')
    file=options.FILE
    song=AudioSegment.from_file(file)
    song.export(f"{actual_folder}audio.mp3", format="mp3")
    file=f"{actual_folder}audio.mp3"

    video1_audio=audio.Audio(f"{file}")
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
           print(f'Processing {i}')
           liste_musique.append(nom)

        except KeyError:
           print(f'Processing {i}')
    
    
    

    liste_finale=list(set(liste_musique))
    if len(liste_finale)==0:
       liste_finale.append('No music found in this video')
    for i in liste_finale:
      print(f'Music found : {i}')
      

if __name__ == '__main__':
    main()