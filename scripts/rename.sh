#! /bin/bash
DIR=`pwd`
cd frames
COUNT=1
for DATASET in `ls`
do
    for CLASS in `ls $DATASET`
    do
        for VIDEO in `ls $DATASET/$CLASS`
        do
            for FRAME in `ls $DATASET/$CLASS/$VIDEO`
            do
                VID=$(echo "$COUNT.avi" | cut -d'.' -f 1)    
                mv $DIR/frames/$DATASET/$CLASS/$VIDEO/$FRAME $DIR/frames/$DATASET/$CLASS/$VIDEO/$COUNT
                (( COUNT++ ))
            done
        done
    done
done