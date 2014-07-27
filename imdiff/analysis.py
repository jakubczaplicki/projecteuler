#
# Try to tell the difference between the images
#

import sys, os
import cv2
import numpy

def analyse():
  inimg = cv2.imread('Lenna.png')
  outimg = cv2.imread('LennaR.png')
  bi, gi, ri = cv2.split(inimg)
  bo, go, ro = cv2.split(outimg)
  
  bi = numpy.asarray(bi)
  bo = numpy.asarray(bo)
  print bo
  errR = (ro - ri)**2;
  errG = (go - gi)**2;
  errB = (bo - bi)**2;
  
  n = float(inimg.size) / 3 #divide by 3 to get the number of image pixels
  print  errB.sum()
  print sum(errB)
  MSER = errR.sum() / n
  MSEG = errG.sum() / n
  MSEB = errB.sum() / n
  print MSER, MSEG, MSEB

  #PSNR = 20*log10(255) - 10*log10(MSE)

analyse()

