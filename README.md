# Audio Data

## dependencies
pydub  
librosa  

## use
1. create directories  
from root:  
 ```
 chmod +x start.sh  
./start.sh
 ```

2. how to extract audio from youtube:
install `brew install youtube-dl`  
from command line:  
cd to dir  
run `youtube-dl -x --audio-format 'mp3' url`  


3. put audio files in main directory and run `python split_audio.py`  
use only mp3 or wav files  
naming format for audio files: "Artist's Name - Song Title.ext"  
put samples in /genre/split   
put full files in /genre/full  


## resourses

https://www.ntnu.edu/documents/1001201110/1266017954/DAFx-15_submission_43_v2.pdf  
