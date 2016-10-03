#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

#File names
NAME="test_"
LIBRARY="california"
VERSION="_sps4_yuv_average"
ENC_FOLDER="enc_images"
DEC_FOLDER_BMP="dec_images_bmp"
DEC_FOLDER_YUV="dec_images_yuv"
DEC_FORMAT=".yuv"

#LHE parameters
ql=25
pix_fmt=yuv420p

MAIN_DIRECTORY=$NAME$LIBRARY$VERSION
ENC_DIRECTORY=$MAIN_DIRECTORY/$ENC_FOLDER
DEC_DIRECTORY_BMP=$MAIN_DIRECTORY/$DEC_FOLDER_BMP
DEC_DIRECTORY_YUV=$MAIN_DIRECTORY/$DEC_FOLDER_YUV
RESULTS_FILE=$NAME$LIBRARY$VERSION/results_$LIBRARY$VERSION.csv 

mkdir $MAIN_DIRECTORY
mkdir $ENC_DIRECTORY
mkdir $DEC_DIRECTORY_BMP
mkdir $DEC_DIRECTORY_YUV

echo "Imagen; Ybpp; Tiempo; PSNR_Y;">>$RESULTS_FILE

for f in `ls $LIBRARY`
do
	nombre="${f%.*}"
	echo -n "$nombre;">>$RESULTS_FILE
	#encode
	ffmpeg -loglevel panic -i $LIBRARY/$f -ql $ql -pix_fmt $pix_fmt $ENC_DIRECTORY/$nombre.lhe 2>>$RESULTS_FILE
	#decode YUV
	ffmpeg -loglevel panic -i $ENC_DIRECTORY/$nombre.lhe -pix_fmt nv12 $DEC_DIRECTORY_YUV/$nombre$DEC_FORMAT
	#decode bmp
	ffmpeg -loglevel panic -i $ENC_DIRECTORY/$nombre.lhe $DEC_DIRECTORY_BMP/$nombre.bmp
	#decode planes
  	ffmpeg -loglevel panic -i $ENC_DIRECTORY/$nombre.lhe -filter_complex "extractplanes=y+u+v[y][u][v]" -map [y] $DEC_DIRECTORY_BMP/${nombre}_y.bmp -map [u] $DEC_DIRECTORY_BMP/${nombre}_u.bmp -map [v] $DEC_DIRECTORY_BMP/${nombre}_v.bmp
	#psnr
	python PSNRtool/main.py $LIBRARY/$f ${LIBRARY}_yuv/$nombre$DEC_FORMAT $DEC_DIRECTORY_YUV/$nombre$DEC_FORMAT >> $RESULTS_FILE 
done

IFS=$SAVEIFS
