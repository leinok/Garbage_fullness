import os, sys

path = "train/small/"
dirs = os.listdir(path)
text_file = open('train.txt', 'a')

def makeList():
	for item in dirs:
		if os.path.isfile(path+item):
			text_file.write(path+item + ' ' + '0\n')
makeList()
text_file.close()

