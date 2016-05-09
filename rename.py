# Rename collected garbage fullness data.
# From IMG_*.jpg --> 10_0001.jpg ....

import os
import glob

path = "/home/lei/research/Locision/data/0428/"
for x in xrange(10, 90, 10):		# folder names are 10%, 20%..80%
	data_path = path + str(x) + "%/"
	files = glob.glob(data_path + 'IMG_*.jpg')
	iterNum = 0
	for img_file in files:
		os.rename(img_file, data_path + str(x) + '_' + str(iterNum).zfill(4) + '.jpg')
		iterNum += 1
