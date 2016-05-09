#!/bin/bash
# change the working directory
# call using: (cd ../../data/0428 && ../../Garbage/Fullness8/helper.sh) 

echo "Making directories if not exists (train, val, test) ..."

for folder in train val test
do
	if [ ! -d $folder ]
	then
		mkdir $folder
	fi
done

echo "Moving images into train, val, test folders ..."

for cur in {10..80..10}
do
	echo "moving $cur% folder ..."
done 

# move 0000 - 0079 (80 imgs) into train

# move 0080 - 0089 (10 imgs) into val

# move 0090 - 0099 (10 imgs) into test
