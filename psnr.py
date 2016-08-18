#*********************************************************************************#
# PSNR Class                                                                      #
# This class contains the methods for psnr calculations                           #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
#*********************************************************************************#

import math

#*********************************************************************************#
#   Function calculatePSNR: This calculates the Peak Signal to Noise Ratio (PSNR) # 
#   of the encoded image, comparing it to the original one.                       #
#   Input: original y array, encoded y array, original cb array, encoded cb array,#
#   original cr array, encoded cr array, number of pixels                         #
#   Output: None, just prints the PSNR                                            #
#*********************************************************************************#

def calculatePSNR(original_y, encoded_y, original_cb, encoded_cb, original_cr, encoded_cr, npix):

        total_y = 0 # Summatory of y squared errors
	total_cb = 0 # Summatory of cr squared errors
	total_cr = 0 # Summatory of cb squared errors
        for i in range(0, len(original_y)): 
                
                dif_y = encoded_y[i] - original_y[i] # Simple error between predicted and original luminance
		dif_cb = encoded_cb[i] - original_cb[i] # Simple error between predicted and original cb
		dif_cr = encoded_cr[i] - original_cr[i] # Simple error between predicted and original cr
                total_y = total_y + pow(dif_y, 2) # We add y square to the summatory
		total_cb = total_cb + pow(dif_cb,2) # We add cb square to the summatory
		total_cr = total_cr + pow(dif_cr,2) # We add cr square to the summatory
                         
        meanSquaredErrorY = float(total_y) / float(npix) # And we get the mean squared error per pixel
        meanSquaredErrorCb = float(total_cb) / float(npix) # And we get the mean squared error per pixel
        meanSquaredErrorCr = float(total_cr) / float(npix) # And we get the mean squared error per pixel
       
	if (meanSquaredErrorY != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioY = float(10 * math.log(255 * 255 / meanSquaredErrorY, 10)) 
        else:
                peakSignalToNoiseRatioY = 0

	if (meanSquaredErrorCb != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioCb = float(10 * math.log(255 * 255 / meanSquaredErrorCb, 10)) 
        else:
                peakSignalToNoiseRatioCb = 0

	if (meanSquaredErrorCr != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioCr = float(10 * math.log(255 * 255 / meanSquaredErrorCr, 10)) 
        else:
                peakSignalToNoiseRatioCr = 0

	print 'Y = ', peakSignalToNoiseRatioY, ' Cb = ', peakSignalToNoiseRatioCb, ' Cr = ', peakSignalToNoiseRatioCr


