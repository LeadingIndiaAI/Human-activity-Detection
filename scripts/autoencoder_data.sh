#! /bin/bash
DIR=`pwd`
cd frames
for DATASET in `ls`
do
  for CLASS in `ls $DATASET`
  do
    COUNT=1
    for VIDEO in `ls $DATASET/$CLASS`
    do
      VID=$(echo "$COUNT.avi" | cut -d'.' -f 1)    
      cp  -a $DIR/frames/$DATASET/$CLASS/$VIDEO/. $DIR/autoencoder_data/
      (( COUNT++ ))
    done
  done
done