#! /bin/bash
DIR=`pwd`
cd dataset
for DATASET in `ls`
do
  for CLASS in `ls $DATASET`
  do
    COUNT=1
    for VIDEO in `ls $DATASET/$CLASS`
    do
      VID=$(echo "$COUNT.avi" | cut -d'.' -f 1)    
      python $DIR/scripts/frame_extractor.py $DIR/dataset/$DATASET/$CLASS/$VIDEO $DIR/frames/$DATASET/$CLASS/$VID
      (( COUNT++ ))
    done
  done
done
