
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
		print "ERROR: You should indicate original image and coder image. \n"

	original = args[0]
	encoded = args[1]

	original_width, original_height, original_npix = getImageData(original)
	encoded_width, encoded_height, encoded_npix = getImageData(original)

	if (original_width != encoded_width or original_height != encoded_height or original_npix != encoded_npix):
		print "ERROR: Images should have same dimensions. \n"

	# Getting YUV values
	original_r, original_g, original_b = getRGB(original, original_npix)
	original_y, original_cb, original_cr = RGBtoYUV(original_r, original_g, original_b)

	encoded_r, encoded_g, encoded_b = getRGB(encoded, encoded_npix)
	encoded_y, encoded_cb, encoded_cr = RGBtoYUV(encoded_r, encoded_g, encoded_b)
	
	calculatePSNR(original_y, encoded_y, original_cb, encoded_cb, original_cr, encoded_cr, original_npix)

