#!/usr/bin/python
#-*-coding:Latin-1 -*
import numpy as np
from matplotlib import pyplot as plt
from skimage import segmentation as seg
from scipy import misc
import tifffile as tiff

image_name='difference_map.tif'
IMAGE = tiff.imread(image_name)

image_ref='IRC.tif'
IMAGE_out = tiff.imread(image_ref)

new_shape='shape_0_new.tif'
shape_new = tiff.imread(new_shape)

I=IMAGE.shape[0]
J=IMAGE.shape[1]

IMAGE_out[:,:,0]=255.0*(IMAGE_out[:,:,0]-np.min(IMAGE_out[:,:,0]))/(np.max(IMAGE_out[:,:,0])-np.min(IMAGE_out[:,:,0]))
IMAGE_out[:,:,1]=255.0*(IMAGE_out[:,:,1]-np.min(IMAGE_out[:,:,1]))/(np.max(IMAGE_out[:,:,1])-np.min(IMAGE_out[:,:,1]))
IMAGE_out[:,:,2]=255.0*(IMAGE_out[:,:,2]-np.min(IMAGE_out[:,:,2]))/(np.max(IMAGE_out[:,:,2])-np.min(IMAGE_out[:,:,2]))

p_col=75.0;

for i in range(I):
	for j in range(J):
		
		
		"""
		if(IMAGE[i,j,1]!=0 and IMAGE[i,j,0]==0):
			IMAGE_out[i,j,0]=((100.0-p_col)*IMAGE_out[i,j,0])/100.0+(p_col*0.0)/100.0
			IMAGE_out[i,j,1]=((100.0-p_col)*IMAGE_out[i,j,1])/100.0+(p_col*0.0)/100.0
			IMAGE_out[i,j,2]=((100.0-p_col)*IMAGE_out[i,j,2])/100.0+(p_col*255.0)/100.0
		"""
		if(IMAGE[i,j,0]!=0 and shape_new[i,j]!=0):
			IMAGE_out[i,j,0]=((100.0-p_col)*IMAGE_out[i,j,0])/100.0+(p_col*0.0)/100.0
			IMAGE_out[i,j,1]=((100.0-p_col)*IMAGE_out[i,j,1])/100.0+(p_col*0.0)/100.0
			IMAGE_out[i,j,2]=((100.0-p_col)*IMAGE_out[i,j,2])/100.0+(p_col*255.0)/100.0
		
		if(IMAGE[i,j,0]!=0 and shape_new[i,j]==0):
			IMAGE_out[i,j,0]=((100.0-p_col)*IMAGE_out[i,j,0])/100.0+(p_col*0.0)/100.0
			IMAGE_out[i,j,1]=((100.0-p_col)*IMAGE_out[i,j,1])/100.0+(p_col*255.0)/100.0
			IMAGE_out[i,j,2]=((100.0-p_col)*IMAGE_out[i,j,2])/100.0+(p_col*0.0)/100.0


image_out_name=image_name[0:len(image_name)-4]+"_colored.png"
misc.imsave(image_out_name,IMAGE_out)

