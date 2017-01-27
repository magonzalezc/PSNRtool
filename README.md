# PSNRtool

This is a python PSNR calculator tool


## How to install (Linux)

1. Install Python 2.7 if you dont have it in your computer.

2. Open a new terminal and type:

  ```
  sudo apt-get install python-pip
  sudo pip install numpy
  sudo pip install pillow
  ```

3. Go to the path where example.py is and execute it with the command:

  ```
  python main.py path_original_image path_original_image_yuv_format path_encoded_image_yuv_format
  ```


## Example

  python main.py lena.bmp lena.yuv lena_jpeg.yuv

##More

There are some scripts in Scripts folder:

*transform_to_yuv* : it allows to transform all the images from a directory into yuv format images
*test_psnr_yuv*: it allows to encode all the images from a yuv directory into images with .lhe format (using ffmpeg). In addition, it saves the statistics of bpp, runtime and psnr into results file.

##yuv_nv12_viewer
Usage:

  ```
  python yuv_nv12_viewer.py image.yuv width height
  ```
