#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

image1 = Image.open("1.png")
image2 = Image.open("2.png")
image3 = Image.open("3.png")
image4 = Image.open("4.png")
image5 = Image.open("5.png")
image6 = Image.open("6.png")
image7 = Image.open("7.png")
image8 = Image.open("8.png")

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 5
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

# Make image fit our screen.
image1.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image3.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image4.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image5.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image6.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image7.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image8.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

print("Press CTRL-C to stop.")
double_buffer = matrix.CreateFrameCanvas()
img_width, img_height = image1.size
xpos = 0
while True:
    try:
        xpos += 1
        if xpos > img_width * 9:
            xpos = 0

        double_buffer.SetImage(image1.convert('RGB'), -xpos + img_width)
        double_buffer.SetImage(image2.convert('RGB'), -xpos + img_width * 2)
        double_buffer.SetImage(image3.convert('RGB'), -xpos + img_width * 3)
        double_buffer.SetImage(image4.convert('RGB'), -xpos + img_width * 4)
        double_buffer.SetImage(image5.convert('RGB'), -xpos + img_width * 5)
        double_buffer.SetImage(image6.convert('RGB'), -xpos + img_width * 6)
        double_buffer.SetImage(image7.convert('RGB'), -xpos + img_width * 7)
        double_buffer.SetImage(image8.convert('RGB'), -xpos + img_width * 8)

        double_buffer = matrix.SwapOnVSync(double_buffer)
        time.sleep(0.01)
    except KeyboardInterrupt:
        sys.exit(0)
