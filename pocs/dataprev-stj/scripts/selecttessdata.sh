#! /bin/bash

datatype=$1

LEGTESSDATA=../tessdata/leg/por.traineddata
FASTTESSDATA=../tessdata/fast/por.traineddata
BESTESSDATA=../tessdata/best/por.traineddata

TESSDATA=/usr/local/share/tessdata

if [ "$datatype" == "-l" ]; then
	echo "Tessdata is being changed to Legacy."
	sudo cp $LEGTESSDATA $TESSDATA
	export TESSDATATYPE="LEGACY"
elif [ "$datatype" == "-f" ]; then
	echo "Tessdata is being changed to Fast."
	sudo cp $FASTTESSDATA $TESSDATA
	export TESSDATATYPE="FAST"
elif [ "$datatype" == "-b" ]; then
	echo "Tessdata is being changed to Best."
	sudo cp $BESTESSDATA $TESSDATA
	export TESSDATATYPE="BEST"
fi
