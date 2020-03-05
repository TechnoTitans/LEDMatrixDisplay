#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

#import PIL
#import Image
#import ImageDraw
#import time
#from rgbmatrix import Adafruit_RGBmatrix

import time
from samplebase import SampleBase
from PIL import Image

maxHeight = 32

class imageScrolling(SampleBase):
        def __init__(self, *args, **kwargs):
                super(imageScrolling, self).__init__(*args, **kwargs)
                self.parser.add_argument("-i", "--image", help="The image to display", default="../../examples-api-use/runtext.ppm")

        def run(self):
                #if not 'image' in self.__dict__:
                #    self.image = Image.open(self.args.image).convert('RGB')
                #self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                print 'run'
                img  = Image.open('TechnoTitans.png').convert('RGB')
                img2 = Image.open('1683.png').convert('RGB')
                img3 = Image.open('nordson-logo.png').convert('RGB')
                img.load()
                img2.load()
                img3.load()
                img  = Scale(img)
                img2 = Scale(img2)
                img3 = Scale(img3)

                double_buffer = self.matrix.CreateFrameCanvas()
                #img_width, img_height = self.image.size

                # let's scroll
                xpos = 0
                while True:
                    #xpos += 1
                    #if (xpos > img_width):
                    #    xpos = 0
                
                    #double_buffer.SetImage(self.image, -xpos)
                    #double_buffer.SetImage(self.image, -xpos + img_width)
                    print 'loop'
                    for n in range(32, -img.size[0], -1):
                        double_buffer.SetImage(img, n, 1)
                        double_buffer = self.matrix.SwapOnVSync(double_buffer)
                        time.sleep(0.025)

                    for n in range(32, -img2.size[0], -1):
                        double_buffer.SetImage(img2, n, 1)
                        double_buffer = self.matrix.SwapOnVSync(double_buffer)
                        time.sleep(0.025)

                    for n in range(32, -img3.size[0], -1):
                        double_buffer.SetImage(img3, n, 1)
                        double_buffer = self.matrix.SwapOnVSync(double_buffer)
                        time.sleep(0.025)

        

def Scale(img):
        hpercent = (maxHeight/float(img.size[1]))
        width = int((float(img.size[0])*float(hpercent)))
        img = img.resize((width,maxHeight), Image.ANTIALIAS)
        #print img.size
        return img
        
#MAIN

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = imageScrolling()
    if (not image_scroller.process()):
        image_scroller.print_help()
