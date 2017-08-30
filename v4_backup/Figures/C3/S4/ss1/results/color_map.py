#!/usr/bin/python
#-*-coding:Latin-1 -*
import numpy as np
from matplotlib import pyplot as plt
from skimage import segmentation as seg
from scipy import misc
import tifffile as tiff

image_name='shape_0_new.tif'
IMAGE = tiff.imread(image_name)

I=IMAGE.shape[0]
J=IMAGE.shape[1]

image_out=np.zeros((I,J,3))

dp=0;

for i in range(I):
	for j in range(J):
		if(100.0*i/(I-1)>=dp):
			print 100.0*i/(I-1),"%"
			dp=dp+5
		l=IMAGE[i,j]
		if(l==1):
			image_out[i,j,:]=[255,000,000]
		elif(l==2):
			image_out[i,j,:]=[000,255,000]
		elif(l==3):
			image_out[i,j,:]=[000,000,255]
		elif(l==4):
			image_out[i,j,:]=[255,255,000]
		elif(l==5):
			image_out[i,j,:]=[255,000,255]
		elif(l==6):
			image_out[i,j,:]=[000,255,255]
		elif(l==7):
			image_out[i,j,:]=[255,127,000]
		elif(l==8):
			image_out[i,j,:]=[255,000,127]
		elif(l==9):
			image_out[i,j,:]=[127,255,000]
		elif(l==10):
			image_out[i,j,:]=[000,255,127]
		elif(l==11):
			image_out[i,j,:]=[127,000,255]
		elif(l==12):
			image_out[i,j,:]=[000,127,255]
		elif(l==13):
			image_out[i,j,:]=[127,000,000]
		elif(l==14):
			image_out[i,j,:]=[000,127,000]
		elif(l==15):
			image_out[i,j,:]=[000,000,127]
		elif(l==16):
			image_out[i,j,:]=[127,127,000]
		elif(l==17):
			image_out[i,j,:]=[127,000,127]
		elif(l==18):
			image_out[i,j,:]=[000,127,127]
		elif(l==19):
			image_out[i,j,:]=[127,127,127]
		

image_out_name=image_name[0:len(image_name)-4]+"_colored.png"
misc.imsave(image_out_name,image_out)

