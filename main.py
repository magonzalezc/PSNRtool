# *********************************************************************************#
# PSNRtool                                                                        #
# PSNRtool allows to calculate PSNR of two images                                 #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
# *********************************************************************************#

import sys
from optparse import OptionParser

from imageReader import *
from psnr import *


def print_usage():
    print('USAGE: {} ORIGINAL ENCODED'.format(sys.argv[0]))


if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()

    if len(args) < 2:
        print_usage()

    original = args[0]
    encoded = args[1]

    original_width, original_height, original_npix = get_image_data(original)
    encoded_width, encoded_height, encoded_npix = get_image_data(original)

    if original_width != encoded_width or original_height != encoded_height or original_npix != encoded_npix:
        print("ERROR: Images should have same dimensions. \n")
        exit(1)

    # Getting YUV values
    original_y, original_cb, original_cr = get_yuv(original)
    encoded_y, encoded_cb, encoded_cr = get_yuv(encoded)

    calculate_psnr(original_y, encoded_y, original_cb, encoded_cb, original_cr, encoded_cr, original_npix)
