# Author : sherin.s@gmail.com (Sherin Sasidhan)
# Date   : 05-Oct-2010
 
import Image
import sys
from struct import *
import array
 
if len(sys.argv) != 4:
        print "***** Usage syntax Error!!!! *****\n"
        print "Usage:"
        print "python display-image.py image_name.yuv width height "
        sys.exit(1) # exit
else:
        pass
 
image_name = sys.argv[1]
width = int(sys.argv[2]) #This is necesary because width and height are not in yuv file
height = int(sys.argv[3])
y = array.array('B')
u = array.array('B')
v = array.array('B')
 
f_y = open(image_name, "rb")
f_uv = open(image_name, "rb")
f_uv.seek(width*height, 1)
 
image_out = Image.new("RGB", (width, height))
pix = image_out.load()
 
print "width=", width, "height=", height
 
for i in range(0, height/2):
    for j in range(0, width/2):
        u.append(ord(f_uv.read(1)));
        v.append(ord(f_uv.read(1)));
 
for i in range(0,height):
    for j in range(0, width):
        y.append(ord(f_y.read(1)));
        #print "i=", i, "j=", j , (i*width), ((i*width) +j)
        #pix[j, i] = y[(i*width) +j], y[(i*width) +j], y[(i*width) +j]
        Y_val = y[(i*width)+j]
        U_val = u[((i/2)*(width/2))+(j/2)]
        V_val = v[((i/2)*(width/2))+(j/2)]
        B = 1.164 * (Y_val-16) + 2.018 * (U_val - 128)
        G = 1.164 * (Y_val-16) - 0.813 * (V_val - 128) - 0.391 * (U_val - 128)
        R = 1.164 * (Y_val-16) + 1.596*(V_val - 128)
        pix[j, i] = int(R), int(G), int(B) # update 31/07/2013 for a data type error. thanks Bink for pointing out this. 
 
######################################################
# B = 1.164(Y - 16)                   + 2.018(U - 128)
# G = 1.164(Y - 16) - 0.813(V - 128) - 0.391(U - 128)
# R = 1.164(Y - 16) + 1.596(V - 128)
######################################################
 
image_out.save("out.bmp")
image_out.show()
