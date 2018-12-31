#! /bin/bash
DIR=`pwd`
cd dataset
for CLASS in `ls`
do
  COUNT=1
  for VIDEO in `ls $CLASS`
  do
    VID=$(echo "$COUNT.avi" | cut -d'.' -f 1)    
    python $DIR/frame_extractor.py $DIR/dataset/$CLASS/$VIDEO $DIR/frame/$CLASS/$VID
    (( COUNT++ ))
  done
done
