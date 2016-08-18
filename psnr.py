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

        error_y = 0 # Summatory of y squared errors
	error_cb = 0 # Summatory of cr squared errors
	error_cr = 0 # Summatory of cb squared errors
        for i in range(0, len(original_y)): 
                
                dif_y = abs(original_y[i] - encoded_y[i])    # Simple error between predicted and original luminance
		dif_cb = abs(original_cb[i] - encoded_cb[i]) # Simple error between predicted and original cb
		dif_cr = abs(original_cr[i] - encoded_cr[i]) # Simple error between predicted and original cr
                error_y += dif_y*dif_y    # We add y square to the summatory
		error_cb += dif_cb*dif_cb # We add cb square to the summatory
		error_cr += dif_cr*dif_cr # We add cr square to the summatory
                         
        meanSquaredErrorY = float(error_y) / float(npix) # And we get the mean squared error per pixel
        meanSquaredErrorCb = float(error_cb) / float(npix) # And we get the mean squared error per pixel
        meanSquaredErrorCr = float(error_cr) / float(npix) # And we get the mean squared error per pixel
       
	if (meanSquaredErrorY != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioY = float(-10.0 * math.log(meanSquaredErrorY/(255 * 255), 10)) 
        else:
                peakSignalToNoiseRatioY = 0

	if (meanSquaredErrorCb != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioCb = float(-10.0 * math.log(meanSquaredErrorCb/(255 * 255), 10)) 
        else:
                peakSignalToNoiseRatioCb = 0

	if (meanSquaredErrorCr != 0):
		# We use 255*255 because we're using 8 bits for every luminance value
                peakSignalToNoiseRatioCr = float(-10.0 * math.log(meanSquaredErrorCr/(255 * 255), 10)) 
        else:
                peakSignalToNoiseRatioCr = 0

	print 'Y = ', peakSignalToNoiseRatioY, ' Cb = ', peakSignalToNoiseRatioCb, ' Cr = ', peakSignalToNoiseRatioCr


