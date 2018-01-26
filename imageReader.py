# *********************************************************************************#
# ImageReader Class                                                               #
# This class contains the methods to read the image data                          #
# Author: Marina Gonzalez                                                         #
# Author: Eduardo Rodes Pastor                                                    #
# *********************************************************************************#
from PIL import Image


def get_image_data(filename):
    """
    This gets the width and height of an image (in pixels) and the total number of pixels of it.
    :param filename: image file
    :return: width, height, number of pixels
    """
    im = Image.open(filename)
    width = im.size[0]
    height = im.size[1]
    npix = im.size[0] * im.size[1]

    return width, height, npix


def get_rgb(filename, npix):
    """
    This gets the RGB values from a given file and saves them in three lists from a given file.
    :param filename: image file
    :param npix:  number of pixels
    :return: r, g, b
    """
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
            rpix, gpix, bpix = rgb_im.getpixel((x, y))
            r[im.size[0] * y + x] = rpix
            g[im.size[0] * y + x] = gpix
            b[im.size[0] * y + x] = bpix

    return r, g, b


def get_yuv(filename):
    """
    This gets the YCbCr values from a given file and saves them in three lists from a given file.
    :param filename: image file
    :return: y, u, v
    """
    # Getting image pixels RGB values
    im = Image.open(filename)
    im = im.convert('YCbCr')

    y = []
    u = []
    v = []

    for pix in list(im.getdata()):
        y.append(pix[0])
        u.append(pix[1])
        v.append(pix[2])

    return y, u, v

def rgb_to_yuv(r, g, b):  # in (0,255) range
    """
     This converts three lists (red, blue, green) in their equivalent YUV lists.
    :param r:
    :param g:
    :param b:
    :return: Y, Cb, Cr
    """
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
