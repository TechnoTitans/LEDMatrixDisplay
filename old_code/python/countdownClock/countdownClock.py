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
import datetime
from samplebase import SampleBase
from PIL import Image
from rgbmatrix import graphics

maxHeight = 32
stopBuild = {2019,3,14,17,30,0}

class displayElement:
    element   = None
    inEffect  = ''
    Color     = None
    delay     = 0


class countdownClock(SampleBase):
    dispElemList = []
        
    def __init__(self, *args, **kwargs):
        super(countdownClock, self).__init__(*args, **kwargs)
        self.parser.add_argument("-f", "--file", help="The file to read", default="signContent.txt")

    def run(self):
        if not 'file' in self.__dict__:
            self.file = self.args.file
            print 'run'
                        
            # main loop
            try:
                double_buffer = self.matrix.CreateFrameCanvas()
                de = displayElement()
                de.delay = 0.5
                de.Color = graphics.Color(0,255,0)

                tEnd = datetime.datetime(2019,3,14,17,30,0).replace(microsecond = 0)
                print tEnd
                #print time.asctime(time.localtime(tEnd))
                
                while True:
                    tNow = datetime.datetime.now().replace(microsecond = 0)
                    tdiff = tEnd - tNow
                    de.element = str(tdiff)
                    #de.element = de.element[:-3]
                    #print de.element
                    self.displayText(de, double_buffer)
                                        
            except:
                print "shutting down"


    def displayText(self, de, canvas):
        font = graphics.Font()
        #font.LoadFont("../../fonts/10x20.bdf")
        font.LoadFont("../../fonts/10x20.bdf")
        textColor = de.Color
        center = canvas.width/2
        len = graphics.DrawText(canvas, font, 0, 0, textColor, de.element)
        pos = center - (len/2)
        canvas.Clear()
        len = graphics.DrawText(canvas, font, pos, 20, textColor, de.element)         
        canvas = self.matrix.SwapOnVSync(canvas)
        time.sleep(float(de.delay))
        
#MAIN

if __name__ == "__main__":
    clock = countdownClock()
    if (not clock.process()):
        countdownClock.print_help()
