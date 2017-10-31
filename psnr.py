# *********************************************************************************#
# PSNR Class                                                                      #
# This class contains the methods for psnr calculations                           #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
# *********************************************************************************#

import math


def calculate_psnr(original_y, encoded_y, original_cb, encoded_cb, original_cr, encoded_cr, npix):
    """
    This calculates the Peak Signal to Noise Ratio (PSNR) of the encoded image, comparing it to the original one.
    :param original_y:
    :param encoded_y:
    :param original_cb:
    :param encoded_cb:
    :param original_cr:
    :param encoded_cr:
    :param npix:
    :return:
    """
    error_y = 0  # Summatory of y squared errors
    error_cb = 0  # Summatory of cr squared errors
    error_cr = 0  # Summatory of cb squared errors
    for i in range(0, len(original_y)):
        dif_y = abs(original_y[i] - encoded_y[i])  # Simple error between predicted and original luminance
        dif_cb = abs(original_cb[i] - encoded_cb[i])  # Simple error between predicted and original cb
        dif_cr = abs(original_cr[i] - encoded_cr[i])  # Simple error between predicted and original cr
        error_y += dif_y * dif_y  # We add y square to the summatory
        error_cb += dif_cb * dif_cb  # We add cb square to the summatory
        error_cr += dif_cr * dif_cr  # We add cr square to the summatory

    mse_y = float(error_y) / float(npix)  # And we get the mean squared error per pixel
    mse_cb = float(error_cb) / float(npix)  # And we get the mean squared error per pixel
    mse_cr = float(error_cr) / float(npix)  # And we get the mean squared error per pixel

    if mse_y != 0:
        # We use 255*255 because we're using 8 bits for every luminance value
        psnr_y = float(-10.0 * math.log(mse_y / (255 * 255), 10))
    else:
        psnr_y = 0

    if mse_cb != 0:
        # We use 255*255 because we're using 8 bits for every luminance value
        psnr_cb = float(-10.0 * math.log(mse_cb / (255 * 255), 10))
    else:
        psnr_cb = 0

    if mse_cr != 0:
        # We use 255*255 because we're using 8 bits for every luminance value
        psnr_cr = float(-10.0 * math.log(mse_cr / (255 * 255), 10))
    else:
        psnr_cr = 0

    print('Y = ', psnr_y, ' Cb = ', psnr_cb, ' Cr = ', psnr_cr)
