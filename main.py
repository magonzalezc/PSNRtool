
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
	
	if (len(args) < 2):
		print "ERROR: You should indicate original bmp image and encoded yuv image. \n"


	original = args[0]
	encoded_yuv = args[1]

	original_width, original_height, original_npix = getImageData(original)

	# Compare original image with encoded image with NV12 format
	original_r, original_g, original_b = getRGB(original, original_npix)
	original_y, original_cb, original_cr = RGBtoYUV(original_r, original_g, original_b)
	encoded_y, encoded_cb, encoded_cr = getYUV(encoded_yuv, original_width, original_height)
	
	calculatePSNR_Y(original_y, encoded_y, original_npix)

