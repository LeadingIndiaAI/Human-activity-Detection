set PWD_new (pwd)
cd dataset
for CLASS in (ls)
  cd $CLASS
  for VIDEO in (ls)
    mkdir $PWD_new/frames/$CLASS/$VIDEO
    python $PWD_new/frame_extractor.py $PWD_new/frames/$CLASS/$VIDEO
  end
end  
