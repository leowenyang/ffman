# -*- coding: utf8 -*-

from ffman.ffmpeg.framework.ffprobe import *
from ffman.ffmpeg.framework.parameters import *

class AVProb(object):
    """docstring for FFProbeFactory"""
    def __init__(self, inFile):
        self.input = Input('"'+inFile+'"')
        self.input.add_formatparam('-hide_banner', None)
        self.output = Output(None)

    def getVideoLen(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-show_entries', 'format=duration')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
            result = float(result[0].decode('utf-8'))
        return result

    def getVideoSize(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-show_entries', 'format=size')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
            result = int(result[0].decode('utf-8'))
        return result

    def getVideoWidth(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-select_streams', 'v:0')
        self.input.add_formatparam('-show_entries', 'stream=width')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
            result = int(result[0].decode('utf-8'))
        return result

    def getVideoHeight(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-select_streams', 'v:0')
        self.input.add_formatparam('-show_entries', 'stream=height')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
            result = int(result[0].decode('utf-8'))
        return result

    def getVideoFrameRate(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-select_streams', 'v:0')
        self.input.add_formatparam('-show_entries', 'stream=avg_frame_rate')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
            result = result[0].decode('utf-8')
            result = eval(result)
        return result

    def getVideoFrames(self):
        self.input.add_formatparam('-v', 'error')
        self.input.add_formatparam('-count_frames', None)
        self.input.add_formatparam('-select_streams', 'v:0')
        self.input.add_formatparam('-show_entries', 'stream=nb_read_frames')
        self.input.add_formatparam('-of', 'default=noprint_wrappers=1:nokey=1')

        result = self.run()
        if len(result) == 1:
          result = int(result[0].decode('utf-8'))
        return result

    """
    Other Handle
    """
    def run(self):
        return FFProbe('ffprobe', self.input, self.output).run()

def main():
    ffprobe = AVProb("input.mp4")
    print(ffprobe.getVideoFrames())

if __name__ == '__main__':
    main()