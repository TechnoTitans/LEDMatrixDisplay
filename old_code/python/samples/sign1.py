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
        ImageList = []
        
        def __init__(self, *args, **kwargs):
                super(imageScrolling, self).__init__(*args, **kwargs)
                self.parser.add_argument("-f", "--file", help="The file to read", default="signContent.txt")

        def run(self):
                if not 'file' in self.__dict__:
                    self.file = self.args.file
                print 'run'
                self.readFile()
                img  = Image.open('TechnoTitans.png').convert('RGB')
                img.load()
                img  = Scale(img)

                double_buffer = self.matrix.CreateFrameCanvas()
                #img_width, img_height = self.image.size

                # let's scroll
                xpos = 0
                while True:
                    for img in self.ImageList:
                        self.ScrollImage(img, double_buffer)

        def ScrollImage(self, img, canvas):
                for n in range(32, -img.size[0], -1):
                    canvas.SetImage(img, n, 1)
                    canvas = self.matrix.SwapOnVSync(canvas)
                    time.sleep(0.025)
                
        def readFile(self):
            #f = open("signContent.txt", "r")
            f = open(self.file, "r")
            for line in f.readlines():
                v = line.split(",")
                if v[0] == "file":
                    fileName = v[1].rstrip()
                    img  = Image.open(fileName).convert('RGB')
                    img.load()
                    img  = Scale(img)
                    self.ImageList.append(img)

            f.close()
            
        

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
