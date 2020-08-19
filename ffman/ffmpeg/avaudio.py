# -*- coding: utf8 -*-

from ffman.ffmpeg.framework.ffmpeg import *
from ffman.ffmpeg.framework.parameters import *

class AVAudio(object):
    """docstring for FFMpegFactory"""
    def __init__(self, inFile, outFile):
        self.input = Input('"'+inFile+'"')
        self.input.add_formatparam('-hide_banner', None)
        self.output = Output('"'+outFile+'"')

    def addMergeMusic(self, music):
        # Input
        #self.input.add_formatparam('-stream_loop', '100')
        self.input.add_formatparam('-i', '"'+music+'"')
        # Output
        strFilter = '"[0:a][1:a]amix=duration=first,pan=stereo|c0<c0+c1|c1<c2+c3,pan=mono|c0=c0+c1[a]"'
        # strFilter = '"[1:a]volume=1[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=0[a]"'
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map_metadata', '-1')
        self.output.add_formatparam('-map', '1:v')
        self.output.add_formatparam('-map', '[a]')
        self.mp4Format()
        # self.output.add_formatparam('-shortest', None)
        self.output.add_formatparam('-ac', '2')
        self.output.add_formatparam('-b', '4M')

    def splitAudio(self):
        # Output
        strFilter = 'volume=2.3'
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-vn', None)
        self.output.add_formatparam('-b:a', '128k')
        self.output.add_formatparam('-ar', '48000')
        self.output.add_formatparam('-ac', '2')

    def mergeAudio(self, file):
        # Input
        self.input.add_formatparam('-i', '"'+file+'"')
        # Output
        self.output.add_formatparam('-map_metadata', '-1')
        self.output.add_formatparam('-map', '1:v')
        self.output.add_formatparam('-map', '0:a')
        self.mp4Format()
        # strFilter = '"[0:a]pan=stereo|c0<c0+c1|c1<c2+c3,pan=mono|c0=c0+c1[a]"'
        # # strFilter = '"[1:a]volume=1[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=0[a]"'
        # self.output.add_formatparam('-filter_complex', strFilter)
        # self.output.add_formatparam('-map_metadata', '-1')
        # self.output.add_formatparam('-map', '1:v')
        # self.output.add_formatparam('-map', '[a]')
        # self.mp4Format()

    def addMusic(self, music):
        # Input
        #self.input.add_formatparam('-stream_loop', '100')
        self.input.add_formatparam('-i', '"'+music+'"')
        # Output
        self.output.add_formatparam('-map_metadata', '-1')
        self.output.add_formatparam('-map', '1:v:0')
        self.output.add_formatparam('-map', '0:a:0')
        self.mp4Format()
        # self.output.add_formatparam('-shortest', None)
        # self.output.add_formatparam('-b', '4M')

    def addNullAudio(self, nullFile):
        # Input
        self.input.add_formatparam('-i', '"'+nullFile+'"')
        # Output
        self.output.add_formatparam('-c:v', 'copy')
        self.output.add_formatparam('-c:a', 'aac')
        self.output.add_formatparam('-b:a', '128k')
        self.output.add_formatparam('-ar', '48000')
        self.output.add_formatparam('-ac', '2')
        self.output.add_formatparam('-shortest', None)

    def creatMuteAudio(self, duration):
        #ffmpeg -f lavfi -t 10 -i anullsrc test.aac -y
        self.input.add_formatparam('-f' 'lavfi')
        self.input.add_formatparam('-t', duration)
        # # Input
        # self.input.add_formatparam('-ss', '0')
        # self.input.add_formatparam('-accurate_seek', None)


        # # Output
        # self.output.add_formatparam('-t', duration)
        # self.output.add_formatparam('-avoid_negative_ts', '1')
        # self.output.add_formatparam('-seek2any', '1')
        # self.output.add_formatparam('-b:a', '128k')
        # self.output.add_formatparam('-ar', '48000')
        # self.output.add_formatparam('-ac', '2')

    def audioMute(self):
        # Output
        self.output.add_formatparam('-an', None)
        #self.output.add_formatparam('-vcodec', 'copy')

    def audioMix(self, audioFile):
        # Input
        self.input.add_formatparam('-i', '"'+audioFile+'"')
        # Output
        strFilter = 'amix=inputs=2:duration=longest:dropout_transition=2'
        self.output.add_formatparam('-filter_complex', strFilter)

    """
    Other Handle
    """
    def run(self):
        self.output.overwrite()
        return FFmpeg('ffmpeg', self.input, self.output).run()

if __name__ == '__main__':
    main()