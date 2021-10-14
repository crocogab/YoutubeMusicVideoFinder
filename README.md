## YoutubeMusicFinder

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()
![Maintainer](https://img.shields.io/badge/maintainer-Crocogab-blue)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/crocogab/YoutubeMusicFinder/issues)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/crocogab/YoutubeMusicFinder/blob/main/LICENSE)
[![Github tag](https://badgen.net/github/tag/crocogab/YoutubeMusicFinder/)](https://github.com/crocogab/YoutubeMusicFinder/tags)


## Summary about YoutubeMusicFinder

What is YoutubeMusicFinder for?

- Recognize unknown music in a video
- List all music from a youtube video / file and soon with timecode.

For example with this video: https://www.youtube.com/watch?v=QkJIheFSRVo

```
YoutubeMusicFinder.py -u https://www.youtube.com/watch?v=QkJIheFSRVo
...
Music found : Army
Music found : On Fire
Music found : Than
Music found : Lonely Way
```
## Difference between YoutubeMusicFinder and YoutubeMusicFinderFromFile

### YoutubeMusicFinder
YoutubeMusicFinder is used to find music from a youtube video. We must therefore give as argument the url of the video. 
As in the following example:

```
YoutubeMusicFinder.py -u URL
```
### YoutubeMusicFinderFromFile

YoutubeMusicFinderFromFile is used to find the music of an audio.
It is therefore necessary to give as argument the path of the file in mp3.

> **Warning**: it is imperative that the file is called audio.mp3 and is located in the script folder
as in the following example

```
YoutubeMusicFinderFromFile.py -f FILE_PATH
```
### Arguments
You should use :
- -f or --file on YoutubeMusicFinderFromFile file (used to precise url)
- -u or --url on YoutubeMusicFinder file (used to file path)
## Installation
```
cd YoutubeMusicFinder
pip install -r requirements.txt
python YoutubeMusicFinder.py -u URL 
```

[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=crocogab&theme=blue-green)](https://github.com/crocogab)

