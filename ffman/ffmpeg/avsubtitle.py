# -*- coding: utf8 -*-

from ffman.ffmpeg.framework.ffmpeg import *
from ffman.ffmpeg.framework.parameters import *

class AVSubtitle(object):
    """docstring for FFMpegFactory"""
    def __init__(self, inFile, outFile):
        self.input = Input('"'+inFile+'"')
        self.input.add_formatparam('-hide_banner', None)
        self.output = Output('"'+outFile+'"')

    """
    Subtitle Handle
    """
    def addSubtitle(self, txtFile):
        # Output
        strFilter = '"drawtext=fontfile=zhanku.ttf:x=800:y=900:fontsize=72:fontcolor=#FF0000:alpha=0.9:textfile=%s:enable=between(t\,3.5\,6.5)"' \
        % (txtFile)
        self.output.add_formatparam('-filter_complex', strFilter)


    """
    Other Handle
    """
    def run(self):
        self.output.overwrite()
        return FFmpeg('ffmpeg', self.input, self.output).run()

if __name__ == '__main__':
    main()