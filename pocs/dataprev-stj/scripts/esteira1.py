import os
import cv2
import subprocess
import numpy as np 
from matplotlib import pyplot as plt

testpdfdir = '../dataset/test/pdf'
testpngdir = '../dataset/test/png'
testtxtdir = '../dataset/test/txt'

testpngprocdir = '../dataset/test/png-proc'
testtxtprocdir = '../dataset/test/txt-proc'

tesspngfile = 'inputset.txt'



#############################################
# Prepare pngs files to run on Tesseract OCR
#############################################
def setImageDir(pngprocdir):
    pngFiles = os.listdir(pngprocdir)
    pngFiles.sort()
    for pngfile in pngFiles:
        


#########################################################
# Convert all pdf files into png files. 
# Each page on pdf file will result in a .png image file
#########################################################
def imageConvert(pdfDir, pngDir):
    pdfFiles = os.listdir(pdfDir)
    pdfFiles.sort()
    for pdfFile in pdfFiles:
        dirname = pngDir +'/'+ pdfFile.split('.')[0]
        pngFile = dirname + '.png'
        pngFile = pngFile.replace(' ', '_')
        convert = ["convert", 
                   "-density",
                   "288",
                   pdfDir +'/'+ pdfFile,
                   "-quality",
                   "100",
                   pngFile]
                   
        subprocess.call(convert, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#######################################################
# Apply image contours analysis to remove noises.
#######################################################
def imageCountourAnalysis (inputDir):
    pngFiles = os.listdir(inputDir)
    pngFiles.sort()
    for pngFile in pngFiles:
        input_file = testpngprocdir +'/'+ pngFile
        img = cv2.imread(input_file,0)
        im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 
        cv2.drawContours(im2, contours, -1, (0,255,0), 3)
        cv2.imwrite(input_file, im2)

#######################################################
# Apply image processing techniques to enhance text.
#######################################################
def imagePreProcess (inputDir):
    pngFiles = os.listdir(testpngdir)
    pngFiles.sort()
    for pngFile in pngFiles:
        input_file = testpngdir +'/'+ pngFile
        output_file = testpngprocdir +'/'+ pngFile
        img = cv2.imread(input_file, 0)
        hist = cv2.equalizeHist(img)
        dst = cv2.fastNlMeansDenoising(hist, None, 75)
        cv2.imwrite(output_file, dst) 

#######################################################
# Apply OCR method to convert png file into a txt file.
#######################################################
def imageOCR (pngDir, txtDir, language='por', filterType='none'):
    pngFiles = os.listdir(pngDir)
    pngFiles.sort()
    for pngFile in pngFiles:
        input_file = pngDir +'/'+ pngFile            
        output_file = txtDir +'/'+ pngFile.split('.')[0]
        tesseract = ["tesseract",
		              input_file, 
                      output_file, 
                      "--oem", "1",
                      "-l", language]
        subprocess.call(tesseract, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print 'OCR applied on ' + input_file 

#imageOCR(testpngdir, testtxtdir)    
#imageOCR(testpngprocdir, testtxtprocdir)
#imagePreProcess(testpngdir)
imageCountourAnalysis(testpngprocdir)



