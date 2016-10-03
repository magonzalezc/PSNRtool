#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

#File names
LIBRARY="california"
ENC_DIRECTORY=${LIBRARY}_yuv

mkdir $ENC_DIRECTORY

for f in `ls $LIBRARY`
do
	nombre="${f%.*}"
	#encode
	ffmpeg -loglevel panic -i $LIBRARY/$f -pix_fmt nv12 $ENC_DIRECTORY/$nombre.yuv
done

IFS=$SAVEIFS
