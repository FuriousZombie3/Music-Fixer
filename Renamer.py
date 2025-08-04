import os, time
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC
    
os.system("dir > list.txt")
file = open('list.txt','r')
items = file.readlines()
file.close()
files = []
titles = []
artists = []

for item in items:
    if(item.find(".mp3") == -1):
        e = 1
    else:
        temp = item[39:-1]
        files.append(temp) #save file name
        titles.append(temp[:temp.find(" - ")])#gets title
        artists.append(temp[temp.find(" - ") + 3:-4]) #gets artist
        
for i in range(len(files)):
    audio = MP3(files[i])
    # Modify or add album properties
    audio["TALB"] = TALB(encoding=3, text=["My Collection"])  # Set Album Name
    #audio["TPE1"] = TPE1(encoding=3, text=[artists[i]]) # Set Artist Name
    #audio["TIT2"] = TIT2(encoding=3, text=[titles[i]]) # Set Title

    # Save the changes
    audio.save()