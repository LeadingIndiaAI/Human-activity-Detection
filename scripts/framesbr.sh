#! /bin/bash
cd ..
DIR=`pwd`
cd dataset
for DATASET in `ls`
do
  for CLASS in `ls`
  do
    COUNT=1
    for VIDEO in `ls $CLASS`
    do
      VID=$(echo "$COUNT.avi" | cut -d'.' -f 1)    
      python $DIR/scripts/frame_extractor_br.py $DIR/dataset/$CLASS/$VIDEO $DIR/framesBR/$CLASS/$VID
      (( COUNT++ ))
    done
  done
done
