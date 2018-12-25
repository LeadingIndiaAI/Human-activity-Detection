#! /bin/bash
DIR=`pwd`
cd dataset
for CLASS in `ls`
do
  for VIDEO in `ls $CLASS`
  do
    VID=$(echo $VIDEO | cut -d'.' -f 1)    
    python $DIR/frame_extractor.py $DIR/dataset/$CLASS/$VIDEO $DIR/frame/$CLASS/$VID
  done
done
