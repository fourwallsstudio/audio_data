from pydub import AudioSegment
from os import listdir
from os.path import isfile, join

mypath = './'

files = [] 
for f in listdir(mypath):
    if isfile(join(mypath, f)):
        _, ext = f.split('.')
        if ext == 'wav' or ext == 'mp3':
            files.append(f)

for f in files:
    file_name, file_format = f.split('.')
    
    sound = AudioSegment.from_file(f, format=file_format)

    duration = len(sound)
    slice_size = 30000
    start = 0
    i = 0

    while (start + slice_size) <= duration:
        end = start + slice_size
        slice = sound[start:end]
        slice.export("./split/{0}-{1}.{2}".format(file_name, i, file_format), format=file_format)
        start += slice_size
        i += 1
