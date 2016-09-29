#*********************************************************************************#
# ImageReader Class                                                               #
# This class contains the methods to read the image data                          #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
#*********************************************************************************#
from PIL import Image
import array 

#***********************************************************************#
#	Function getImageData: This gets the width and height of an     #
#	image (in pixels) and the total number of pixels of it.         #
#	Input: image file                                               #
#	Output: width (pixels), height (pixels), number of pixels       #
#***********************************************************************#
def getImageData(filename):


	im = Image.open(filename)
	width = im.size[0]
	height = im.size[1]
	npix = im.size[0] * im.size[1]

	return width, height, npix
	
#*********************************************************************************#
#	Function getRGB: This gets the RGB values from a given file and saves     #
#	them in three lists from a given file.                                    #
#	Input: file, number of pixels of the file                                 #
#	Output: r [], g [], b []                                                  #
#*********************************************************************************#
def getRGB(filename, npix):

	# Getting image pixels RGB values
	im = Image.open(filename)
	rgb_im = im.convert('RGB')

	# Creating three lists of npix items
	r = [-1] * npix 
	g = [-1] * npix
	b = [-1] * npix

	for y in range(0, im.size[1]):
		for x in range(0, im.size[0]):

			# We get the RGB value in each pixel and save each component in an array
			rpix, gpix, bpix = rgb_im.getpixel((x,y)) 
			r[im.size[0]*y + x] = rpix
			g[im.size[0]*y + x] = gpix
			b[im.size[0]*y + x] = bpix

	return r, g, b

#***********************************************************************#
#	Function RGBtoYUV: This converts three lists (red, blue, green) #
#	in their equivalent YUV lists.                                  #
#	Input: r [], g [], b []                                         #
#	Output: y [], cb [], cr []                                      #
#***********************************************************************#
def RGBtoYUV(r, g, b): # in (0,255) range

	# All of these lists have the same length
	y = [0] * len(r) 
	cb = [0] * len(r) 
	cr = [0] * len(r)

	# This is just the formula to get YUV from RGB.
	for i in range(0, len(r)): 		
		y[i] = int(0.299 * r[i] + 0.587 * g[i] + 0.114 * b[i])
		cb[i] = int(128 - 0.168736 * r[i] - 0.331364 * g[i] + 0.5 * b[i])
		cr[i] = int(128 + 0.5 * r[i] - 0.418688 * g[i] - 0.081312 * b[i])

	return y, cb, cr

#*********************************************************************************#
#	Function getYUV: This gets the YUV values from a YUV file and saves       #
#	them in three lists from a given file.                                    #
#	Input: file, number of pixels of the file                                 #
#	Output: y [], u [], v []                                                  #
#*********************************************************************************#
def getYUV(filename, width, height):

	y = array.array('B')
	u = array.array('B')
	v = array.array('B')

	f_y = open(filename, "rb")
	f_uv = open(filename, "rb")
	f_uv.seek(width*height, 1)

	for i in range(0, height/2):
		for j in range(0, width/2):
			u.append(ord(f_uv.read(1)));
			v.append(ord(f_uv.read(1)));

	for i in range(0,height):
		for j in range(0, width):
			y.append(ord(f_y.read(1)));
			

	return y, u, v


