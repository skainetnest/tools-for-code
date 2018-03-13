#! /bin/bash

INPUTPNGFILE=$1
OUTPUTTXTFILE=$2
ENGINEMODE=$3

echo "Running Tesseract: Input file: $INPUTPNGFILE"
echo "Running Tesseract: Output file: $OUTPUTTXTFILE"

if [ "$ENGINEMODE" == "-tess" ]; then
    tesseract $INPUTPNGFILE $OUTPUTTXTFILE --oem 0 -l por
elif [ "$ENGINEMODE" == "-lstm" ]; then
    tesseract $INPUTPNGFILE $OUTPUTTXTFILE --oem 1 -l por
elif [ "$ENGINEMODE" == "-tnn" ]; then
    tesseract $INPUTPNGFILE $OUTPUTTXTFILE --oem 2 -l por
fi

