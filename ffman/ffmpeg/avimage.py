# -*- coding: utf8 -*-

from ffman.ffmpeg.framework.ffmpeg import *
from ffman.ffmpeg.framework.parameters import *

class AVImage(object):
    """docstring for FFMpegFactory"""
    def __init__(self, inFile, outFile):
        self.input = Input('"'+inFile+'"')
        self.input.add_formatparam('-hide_banner', None)
        self.output = Output('"'+outFile+'"')

    """
    Image Handle
    """
    # color : #RRGGBB@0.5
    def colorBar(self, x, y, width, height, color):
      self.input.add_formatparam('-f', 'lavfi')
      strColor = 'color=c=%s:s=%sx%s,format=rgba' % (color, width, height)
      self.input.add_formatparam('-i', strColor)
      strFilter = "[1:v][0:v]overlay=x=%s:y=%s:shortest=1[out]" % (x, y)
      self.output.add_formatparam('-filter_complex', strFilter)
      self.output.add_formatparam('-map', '[out]')

    def colorMove(self, x, y, start, end, speed, color, width, height, direct):
       # Input=black:s=1920x1080
      self.input.add_formatparam('-f', 'lavfi')
      strColor = 'color=c=%s:s=%sx%s' % (color, width, height)
      self.input.add_formatparam('-i', strColor)

      # Output
      during = end - start
      # up
      if direct == 1:
        strFilter = "[1:v][0:v]overlay=y='if(between(t,%s,%s),(%s-%s*(t-%s)),if(lte(t,%s),%s,NAN))':x=%s:shortest=1[out]" % (start, end, y, speed, start, start, y, x)
      # down
      elif direct == 2:
        strFilter = "[1:v][0:v]overlay=y='if(between(t,%s,%s),(%s+%s*(t-%s)),if(lte(t,%s),%s,NAN))':x=%s:shortest=1[out]" % (start, end, y, speed, start, start, y, x)
      # left
      elif direct == 3:
        strFilter = "[1:v][0:v]overlay=x='if(between(t,%s,%s),(%s-%s*(t-%s)),if(lte(t,%s),%s,NAN))':y=%s:shortest=1[out]" % (start, end, x, speed, start, start, x, y)
      # right
      elif direct == 4:
        strFilter = "[1:v][0:v]overlay=x='if(between(t,%s,%s),(%s+%s*(t-%s)),if(lte(t,%s),%s,NAN))':y=%s:shortest=1[out]" % (start, end, x, speed, start, start, x, y)
      self.output.add_formatparam('-filter_complex', strFilter)
      self.output.add_formatparam('-map', '[out]')


    """
    Other Handle
    """
    def run(self):
        self.output.overwrite()
        return FFmpeg('ffmpeg', self.input, self.output).run()


if __name__ == '__main__':
    main()