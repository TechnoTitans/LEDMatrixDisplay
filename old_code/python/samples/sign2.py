#!/usr/bin/python


# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import time
from samplebase import SampleBase
from PIL import Image
from rgbmatrix import graphics

maxHeight = 32

class displayElement:
    element = None
    delay = 0
    
class signScrolling(SampleBase):
    dispElemList = []
        
    def __init__(self, *args, **kwargs):
        super(signScrolling, self).__init__(*args, **kwargs)
        self.parser.add_argument("-f", "--file", help="The file to read", default="signContent.txt")

    def run(self):
        if not 'file' in self.__dict__:
            self.file = self.args.file
            print 'run'
            self.readFile()
            double_buffer = self.matrix.CreateFrameCanvas()
 
            # let's scroll
            xpos = 0
            while True:
                for de in self.dispElemList:
                    print type(de)
                    if type(de.element) is str:
                        self.ScrollText(de.element, de.delay, double_buffer)
                    else:
                        self.ScrollImage(de.element, de.delay, double_buffer)

    def ScrollImage(self, img, delay, canvas):
        for n in range(canvas.width, -img.size[0], -1):
            canvas.Clear()
            canvas.SetImage(img, n, 1)
            canvas = self.matrix.SwapOnVSync(canvas)
            if n == 0:
                time.sleep(float(delay))
            else:
                time.sleep(0.025)

                 

    def ScrollText(self, msg, delay, canvas):
        font = graphics.Font()
        font.LoadFont("../../fonts/10x20.bdf")
        textColor = graphics.Color(255, 0, 0)
        pos = canvas.width
        canvas.Clear()
        len = graphics.DrawText(canvas, font, pos, 20, textColor, msg)
        for n in range(canvas.width, -(len + canvas.width), -1):
            canvas.Clear()
            len = graphics.DrawText(canvas, font, n, 20, textColor, msg)

            canvas = self.matrix.SwapOnVSync(canvas)
            if n == 0:
                time.sleep(float(delay))
            else:
                time.sleep(0.025)
                
        

    def readFile(self):
        f = open(self.file, "r")
        for line in f.readlines():
            v = line.split(",")
            print v
            value = v[1].rstrip()
            de = displayElement()
            de.delay = v[2]
            #print value
            if v[0] == "file":
                img  = Image.open(value).convert('RGB')
                img.load()
                img  = Scale(img)
                de.element = img
                self.dispElemList.append(de)
            elif v[0] == "text":
                de.element = value
                self.dispElemList.append(de)

        f.close()
            
        

def Scale(img):
        hpercent = (maxHeight/float(img.size[1]))
        width = int((float(img.size[0])*float(hpercent)))
        img = img.resize((width,maxHeight), Image.ANTIALIAS)
        #print img.size
        return img
        
#MAIN

if __name__ == "__main__":
    sign_scroller = signScrolling()
    if (not sign_scroller.process()):
        sign_scroller.print_help()
