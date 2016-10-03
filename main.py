
#*********************************************************************************#
# PSNRtool                                                                        #
# PSNRtool allows to calculate PSNR of two images                                 #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
#*********************************************************************************#

from optparse import OptionParser
from imageReader import *
from psnr import *

if __name__=='__main__':
	parser = OptionParser()
	(options, args) = parser.parse_args()
	
	if (len(args) < 3):
		print "ERROR: You should indicate original bmp image and encoded yuv image. \n"


	original_bmp = args[0]
	original = args[1]
	encoded = args[2]

	original_width, original_height, original_npix = getImageData(original_bmp)
	original_y, original_cb, original_cr = getYUV(original, original_width, original_height)
	encoded_y, encoded_cb, encoded_cr = getYUV(encoded, original_width, original_height)

	# Compare original image with encoded image with NV12 format
	#original_r, original_g, original_b = getRGB(original, original_npix)
	#original_y, original_cb, original_cr = RGBtoYUV(original_r, original_g, original_b)

	#encoded_r, encoded_g, encoded_b = getRGB(encoded, original_npix)
	#encoded_y, encoded_cb, encoded_cr = RGBtoYUV(encoded_r, encoded_g, encoded_b)
	
	calculatePSNR_Y(original_y, encoded_y, original_npix)

