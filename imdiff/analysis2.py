#
# Try to tell the difference between the images
#

#import cv2
import Image, numpy

def split(img):
  pixels = list(img.getdata())
  r = []
  g = []
  b = []
  for p in pixels:
    r.append(p[0])
    g.append(p[1])
    b.append(p[2])
  rr = numpy.asarray(r)
  gg = numpy.asarray(g)
  bb = numpy.asarray(b)
  return rr,gg,bb

def analyse():
  inimg  = Image.open('Lenna.png')
  outimg = Image.open('LennaR.png') #imread
  #print inimg.getpixel((1,1))
  ri,gi,bi = split(inimg)
  ro,go,bo = split(outimg)

  errR = ro - ri;
  errG = go - gi;
  errB = bo - bi;
  n = float(inimg.size[0] * inimg.size[1])
  MSER = sum(errR) / n
  MSEG = sum(errG) / n
  MSEB = sum(errB) / n
  print MSER, MSEG, MSEB

  #PSNR = 20*log10(255) - 10*log10(MSE)

analyse()

