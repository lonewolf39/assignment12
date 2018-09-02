# Print the current Day

import datetime 
d=datetime.datetime.now()
print(d.day)


#use webbrowser module in python

import webbrowser as web
web.open("https://www.youtube.com/watch?v=DdT1l-etiFs")


# Rename all the files in a Directory and convert them into .jpg file format

import os
path = 'E:\study material'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
