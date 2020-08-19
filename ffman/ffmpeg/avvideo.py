# -*- coding: utf8 -*-

from ffman.ffmpeg.framework.ffmpeg import *
from ffman.ffmpeg.framework.parameters import *

class AVVidoe(object):
    """docstring for FFMpegFactory"""
    def __init__(self, inFile, outFile):
        self.input = Input('"'+inFile+'"')
        self.input.add_formatparam('-hide_banner', None)
        # self.input.add_formatparam('-loglevel', 'verbose')
        # self.input.add_formatparam('-loglevel', 'warning')
        # self.input.add_formatparam('-loglevel', 'error')
        # self.input.add_formatparam('-report', None)
        # self.input.add_formatparam('-hwaccel', 'dxva2')
        # self.input.add_formatparam('-hwaccel', 'qsv')
        # self.input.add_formatparam('-threads', '4')
        # self.input.add_formatparam('-xerror', None)
        self.output = Output('"'+outFile+'"')

    """
    Video Handle
    """
    def outputSarDar(self):
        # Output
        # self.output.add_formatparam('-vf', 'setsar=1:1')
        # self.output.add_formatparam('-vf', 'setdar=16:9')
        self.output.add_formatparam('-vf', 'setsar=1/1')
        self.output.add_formatparam('-vf', 'setdar=16/9')

    def outputFormat(self):
        # Output
        #self.output.add_formatparam('-an', None)
        # self.output.add_formatparam('-s', '1280x720')
        self.output.add_formatparam('-s', '1920x1080')
        # self.output.add_formatparam('-r', '25')
        self.output.add_formatparam('-r', '50')
        self.output.add_formatparam('-pix_fmt', 'yuv420p')
        self.output.add_formatparam('-c:v', 'libx264')
        self.output.add_formatparam('-c:a', 'aac')
        self.output.add_formatparam('-strict', '-2')

        self.output.add_formatparam('-vf', 'setsar=1/1')
        self.output.add_formatparam('-vf', 'setdar=16/9')

        # self.output.add_formatparam('-c:v', 'h264_qsv')
        # self.output.add_formatparam('-look_ahead', '0')
        # self.output.add_formatparam('-b:v', '1.6M')

    def mp4Format_2(self, fRate):
        # Output
        #self.output.add_formatparam('-an', None)
        # self.output.add_formatparam('-s', '1280x720')
        self.output.add_formatparam('-s', '1920x1080')
        self.output.add_formatparam('-pix_fmt', 'yuv420p')
        self.output.add_formatparam('-c:v', 'libx264')
        self.output.add_formatparam('-c:a', 'aac')
        self.output.add_formatparam('-strict', '-2')
        self.output.add_formatparam('-r', fRate)

    def mp4Format(self):
        # Output
        self.output.add_formatparam('-c:v', 'libx264')
        self.output.add_formatparam('-c:a', 'aac')
        self.output.add_formatparam('-strict', '-2')

        # self.output.add_formatparam('-c:v', 'h264_qsv')
        # self.output.add_formatparam('-look_ahead', '0')
        # self.output.add_formatparam('-b:v', '1.6M')

    def videFormat(self):
        # Input
        # Output
        # self.output.add_formatparam('-r', 25)
        self.output.add_formatparam('-r', 50)

    def videoCut(self, start, during=None):
        self.outputSarDar()
        # Input
        self.input.add_formatparam('-ss', start)
        #self.input.add_formatparam('-t', during)
        self.input.add_formatparam('-accurate_seek', None)

        # Output
        if not during is None:
            self.output.add_formatparam('-t', during)
        self.output.add_formatparam('-avoid_negative_ts', '1')
        self.output.add_formatparam('-seek2any', '1')

    def videoCutFrame(self, start, end, muted=True):
        # Output
        if muted:
            strFilter = 'trim=%s:%s,setpts=PTS-STARTPTS' % (start, end)
            self.output.add_formatparam('-filter_complex', strFilter)
        else:
            strFilter = '[0:v]trim=%s:%s,setpts=PTS-STARTPTS[video];[0:a]atrim=%s:%s,asetpts=PTS-STARTPTS[voice]' % (start, end, start, end)
            self.output.add_formatparam('-filter_complex', strFilter)
            self.output.add_formatparam('-map', '[video]')
            self.output.add_formatparam('-map', '[voice]')

    def videoCutAccurate(self, start, end, muted=True):
        # Output
        if muted:
            strFilter = 'trim=%s:%s,setpts=PTS-STARTPTS' % (start, end)
            self.output.add_formatparam('-filter_complex', strFilter)
        else:
            strFilter = '[0:v]trim=%s:%s,setpts=PTS-STARTPTS[video];[0:a]atrim=%s:%s,asetpts=PTS-STARTPTS[voice]' % (start, end, start, end)
            self.output.add_formatparam('-filter_complex', strFilter)
            self.output.add_formatparam('-map', '[video]')
            self.output.add_formatparam('-map', '[voice]')

    def videoCutLossless(self, start, end):
        # Input
        self.input.add_formatparam('-ss', start)

        # Output
        if not end is None:
            self.output.add_formatparam('-t', end)
        self.output.add_formatparam('-c:v', 'copy')
        self.output.add_formatparam('-c:a', 'copy')

    def addFilter(self, filter):
        # Output
        self.output.add_formatparam('-filter_complex', filter)

    def showTime(self, frameRate, time ,startTime, endTime, posX=351, posY=117, fontSize=35, fontcolor='#FFFFFF'):
        # Output
        # time ('09\:57\:00\:00')
        strFilter = "drawtext=fontfile=cour.ttf:fontsize=%s:fontcolor=%s:timecode='%s':r=%s:x=%s:y=%s:enable=between(t\,%s\,%s)" % (fontSize, fontcolor, time, frameRate, posX, posY, startTime, endTime)
        self.output.add_formatparam('-filter_complex', strFilter)

    def showMatchTime(self, frameRate, time ,startTime, endTime, posX=351, posY=117, fontSize=35, fontcolor='#FFFFFF'):
        # Output
        # time ('09\:57\:00\:00')
        strFilter = "drawmatchtime=fontfile=cour.ttf:fontsize=%s:fontcolor=%s:timecode='%s':r=%s:x=%s:y=%s:enable=between(t\,%s\,%s)" % (fontSize, fontcolor, time, frameRate, posX, posY, startTime, endTime)
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoMerge(self):
        # Input
        self.input.add_formatparam('-f', 'concat')
        self.input.add_formatparam('-safe', '0')

        # Output
        self.output.add_formatparam('-c', 'copy')

    def twoVideoMerge(self, videoLen, videFile, overlayDuring):
        # Input
        self.input.add_formatparam('-i', '"'+videFile+'"')

        # Output
        if overlayDuring == 0:
            # all video slow
            strFilter = '[1:v][0:v]concat[out]'
        elif overlayDuring > 0:
            # slow from start
            strFilter = '[1:v]trim=0:%s,setpts=PTS-STARTPTS[v1];'\
                        '[1:v]trim=start=%s,setpts=PTS-STARTPTS[v2];'\
                        '[0:v]colorkey=0x202020:0.3:0.3[ckout];'\
                        '[ckout][v2]overlay=enable=between(t\,0\,%s)[mergeout];'\
                        '[v1][mergeout]concat[out]'\
                        % (videoLen-overlayDuring, videoLen-overlayDuring, overlayDuring)
        else:
            # slow during
            strFilter = '[1:v]trim=0:%s,setpts=PTS-STARTPTS[v1];'\
                        '[1:v]trim=start=%s,setpts=PTS-STARTPTS,colorkey=0x202020:0.3:0.3[v2];'\
                        '[0:v][v2]overlay=enable=between(t\,0\,%s)[mergeout];'\
                        '[v1][mergeout]concat[out]'\
                        % (videoLen+overlayDuring, videoLen+overlayDuring, abs(overlayDuring))

        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def videoScale(self, x, y, width, height):
        # Output
        strFilter = 'crop=%s:%s:%s:%s' % (width, height, x, y)
        self.output.add_formatparam('-filter_complex', strFilter)
        #self.mp4Format_2()
        self.output.add_formatparam('-s', '1920x1080')

    def videoRotate(self, angle):
        # Output (以度表示)
        strFilter = 'rotate=-(%s*PI/180)' % (angle)
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoReverse(self):
        # Output
        strFilter = '[0:v]reverse[r]'
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[r]')

    def videoCBS(self, contrast=1, brightness=0, saturation=1):
        # contrast -2.0 to 2.0. The default value is "1".
        # brightness -1.0 to 1.0. The default value is "0".
        # saturation 0.0 to 3.0. The default value is "1".
        # Output
        strFilter = 'eq=contrast=%s:brightness=%s:saturation=%s' % (contrast, brightness, saturation)
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoLogo(self, imgFile):
        #filter_complex "overlay=0:0:enable=between(t,0,2)"
        # Input
        self.input.add_formatparam('-i', '"'+imgFile+'"')

        # Output
        self.output.add_formatparam('-c:v', 'libx264')
        self.output.add_formatparam('-c:a', 'copy')
        self.output.add_formatparam('-strict', '-2')
        # strFilter = '[0:v]scale=180:80[logo];'\
        #             '[1:v][logo]overlay=main_w-overlay_w-10:main_h-overlay_h-10[out]'
        # strFilter = '[1:v][0:v]overlay=main_w-overlay_w-10:main_h-overlay_h-10[out]'
        strFilter = '[1:v][0:v]overlay=0:0[out]'
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def videoLogo_a(self, imgFile):
        # Input
        self.input.add_formatparam('-i', '"'+imgFile+'"')

        # Output
        strFilter = 'overlay=0:0'
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoToOneImg(self, time):
        # Input
        self.input.add_formatparam('-ss', time)

        # Output
        self.output.add_formatparam('-f', 'image2')
        self.output.add_formatparam('-vframes', '1')

    def videoEndToOneImg(self, time):
        # Input
        self.input.add_formatparam('-sseof', time)

        # Output
        self.output.add_formatparam('-f', 'image2')
        self.output.add_formatparam('-vframes', '1')

    def oneImgToVideo(self, time, width='1920', height='1080', background='black'):
        # Input=black:s=1920x1080
        self.input.add_formatparam('-f', 'lavfi')
        strColor = 'color=%s:s=%sx%s' % (background, width, height)
        self.input.add_formatparam('-i', strColor)
        self.input.add_formatparam('-loop', '1')
        # self.input.add_formatparam('-f', 'image2')

        # Output
        strFilter = '[1:v]scale=-1:%s[pic];[0:v][pic]overlay=x=(W-w)/2:y=(H-h)/2[out]' % (height)
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')
        self.output.add_formatparam('-t', time)

    def videoOverlayVideo(self, file):
        # Input
        self.input.add_formatparam('-i', '"'+file+'"')

        # Output
        strFilter = '[1:v]colorkey=0x333333:0.3:0.2[ckout];'\
                    '[0:v][ckout]overlay[out]'

        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def PIP_videoOnImg(self, videoFile):
        # Input
        # Output
        strFilter = "movie='%s',scale=1280:720,drawbox=color=0xD3D3D3@0.5:t=6,fade=in:st=0:d=0.25[wm];"\
                    "[in]boxblur=3:1[img];"\
                    "[img][wm]overlay=(W-w)/2:(H-h)/2[out]"\
                    % (videoFile)
        self.output.add_formatparam('-vf', strFilter)

    def PIP_imgOnVideo(self, imgFile, start, end):
        # Input
        self.input.add_formatparam('-loop', '1')
        self.input.add_formatparam('-i', '"'+imgFile+'"')

        if int(end) - int(start) > 3:
            during = 1
        else:
            during = 0.5

        # Output
        strFilter = '[0:0]format=rgba,fade=in:st=%s:d=%s:alpha=1,fade=out:st=%s:d=%s:alpha=1[img];'\
                    '[1:0][img]overlay=0:0:shortest=1[out]'\
                     % (start, during, end, during)
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def PIP_imgOnVideo_2(self, imgFile, start, end):
        # Input
        self.input.add_formatparam('-loop', '1')
        self.input.add_formatparam('-i', '"'+imgFile+'"')

        # during = 0

        # # Output
        # strFilter = '[0:0]format=rgba,fade=in:st=%s:d=%s:alpha=1,fade=out:st=%s:d=%s:alpha=1[img];'\
        #             '[1:0][img]overlay=0:0:shortest=1[out]'\
        #              % (start, during, end, during)
        # # Output
        strFilter = '[0:0]format=rgba[img];'\
                    '[1:0][img]overlay=0:0:shortest=1:enable=between(t\,%s\,%s)[out]'\
                     % (start, end)
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def videoFadeIn(self, during):
        # Output
        strFilter = 'fade=t=in:st=0:d=%s' % (during)
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoFadeOut(self, start):
        # Output
        strFilter = 'fade=t=out:st=%s' % (start)
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoSpeed(self, videoStart, videoEnd, slowStart, slowEnd, speed):
        # Input
        # Output
        speed = 1/speed
        #strFilter = '[0:v]setpts=%s*PTS[v]' % (speed)
        if slowStart == videoStart and slowEnd == videoEnd:
            # all video slow
            strFilter = '[0:v]setpts=%s*PTS[out]' % (speed)
        elif slowStart == videoStart:
            # slow from start
            strFilter = '[0:v]trim=0:%s,setpts=PTS-STARTPTS[v1];'\
                        '[0:v]trim=start=%s,setpts=PTS-STARTPTS[v2];'\
                        '[v1]setpts=%s*PTS[slow];[slow][v2]concat[out]'\
                         % (slowEnd, slowEnd, speed)
        elif slowEnd == videoEnd:
            # slow to end
            strFilter = '[0:v]trim=0:%s,setpts=PTS-STARTPTS[v1];'\
                        '[0:v]trim=start=%s,setpts=PTS-STARTPTS[v2];'\
                        '[v2]setpts=%s*PTS[slow];[v1][slow]concat[out]'\
                         % (slowStart, slowStart, speed)
        else:
            # slow during
            strFilter = '[0:v]trim=0:%s,setpts=PTS-STARTPTS[v1];'\
                        '[0:v]trim=%s:%s,setpts=PTS-STARTPTS[v2];'\
                        '[0:v]trim=start=%s,setpts=PTS-STARTPTS[v3];'\
                        '[v2]setpts=%s*PTS[slow];'\
                        '[v1][slow][v3]concat=n=3:v=1:a=0[out]'\
                         % (slowStart, slowStart, slowEnd, slowEnd, speed)

        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-map', '[out]')

    def imgMoveScale(self, during):
        # Input
        self.input.add_formatparam('-loop', '1')
        # Output
        strFilter = "zoompan='if(lte(on,%s*15),zoom+0.003,zoom-0.003)':d=%s*30:fps=30" \
                    % (during, during)
        self.output.add_formatparam('-vf', strFilter)
        self.output.add_formatparam('-t', during)

    def videoMoveScale(self, w1, w2, frame, frameRate):
        # Output
        # (1/e^(ln(w2/w1)/(n-1))^in
        zoom = "pow(1/exp(log(%s/%s)/(%s-1)),in)" % (w2, w1, frame)
        # zoom = "%s*%s/(%s*%s-(%s-%s))" % (frame, w1, frame, w1, w1, w2)
        strFilter = "zoompan=z='%s':s=1920x1080:d=1:x=0:y=0:fps=%s" \
           % (zoom, frameRate)
        #strFilter = "zoompan=z='1+in/1000':d=1:y='if(gte(zoom,1.5),y,y+1)':x='x'"
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoMoveScale_yb(self, x1, y1, w1, h1, x2, y2, w2, h2, frame, frameRate):
        # Output
        speed = '(abs(%s-%s)/%s)*in' % (x2, x1, frame)
        if x2 == x1:
          xPos = '%s' % (x1)
        elif x2 > x1:
          xPos = "'if(gte(%s,%s+%s),(%s+%s),%s)'" % (x2, x1, speed, x1, speed, x2)
        else:
          xPos = "'if(gte(%s-%s,%s),%s-%s,%s)'" % (x1, speed, x2, x1, speed, x2)

        speed = '(abs(%s-%s)/%s)*in' % (y2, y1, frame)
        if y2 == y1:
          yPos = '%s' % (y1)
        elif y2 > y1:
          yPos = "'if(gte(%s,%s+%s),(%s+%s),%s)'" % (y2, y1, speed, y1, speed, y2)
        else:
          yPos = "'if(gte(%s-%s,%s),%s-%s,%s)'" % (y1, speed, y2, y1, speed, y2)

        # (1/e^(ln(w2/w1)/(n-1))^in
        zoom = "pow(exp(log(%s/%s)/(%s-1)),in)" % (w2, w1, frame)
        # zoom = "%s*%s/(%s*%s-(%s-%s))" % (frame, w1, frame, w1, w1, w2)
        strFilter = "zoomscale=z='%s':s=1920x1080:d=1:x=%s:y=%s:w=%s:h=%s:fps=%s" \
           % (zoom, xPos, yPos, w1, h1, frameRate)
        #strFilter = "zoompan=z='1+in/1000':d=1:y='if(gte(zoom,1.5),y,y+1)':x='x'"
        self.output.add_formatparam('-filter_complex', strFilter)

    def cameraMove(self, x, y, frameRate):
        # Output
        strFilter = 'zoompan=z="1+in/800":s=1920x1080:d=1:x=%s:y=%s:fps=%s' % (x, y, frameRate)
        #strFilter = "zoompan=z='1+in/1000':d=1:y='if(gte(zoom,1.5),y,y+1)':x='x'"
        self.output.add_formatparam('-filter_complex', strFilter)
        # self.mp4Format_2('60')

    def cameraWalk(self, srcX, srcY, dstX, dstY, width, height, frames):
        # Output
        speed = '(abs(%s-%s)/%s)*n' % (dstX, srcX, frames)
        if dstX == srcX:
          xPos = '%s' % (srcX)
        elif dstX > srcX:
          xPos = "'if(gte(%s,%s+%s),(%s+%s),%s)'" % (dstX, srcX, speed, srcX, speed, dstX)
        else:
          xPos = "'if(gte(%s-%s,%s),%s-%s,%s)'" % (srcX, speed, dstX, srcX, speed, dstX)

        speed = '(abs(%s-%s)/%s)*n' % (dstY, srcY, frames)
        if dstY == srcY:
          yPos = '%s' % (srcY)
        elif dstY > srcY:
          yPos = "'if(gte(%s,%s+%s),(%s+%s),%s)'" % (dstY, srcY, speed, srcY, speed, dstY)
        else:
          yPos = "'if(gte(%s-%s,%s),%s-%s,%s)'" % (srcY, speed, dstY, srcY, speed, dstY)


        strFilter = '"crop=%s:%s:%s:%s"' % (width, height, xPos, yPos)
        self.output.add_formatparam('-filter_complex', strFilter)

    def vidstabdetect(self):
        # Output
        strFilter = 'vidstabdetect=stepsize=6:shakiness=1:accuracy=9:result=mytransforms.trf'
        self.output.add_formatparam('-filter_complex', strFilter)
        self.output.add_formatparam('-f', 'null')

    def vidstabtransform(self):
        strFilter = 'vidstabtransform=input=mytransforms.trf:zoom=0:maxangle=3*PI/180:smoothing=3,unsharp=5:5:0.8:3:3:0.4'
        self.output.add_formatparam('-filter_complex', strFilter)

    def palettegen(self):
        # Output
        self.output.add_formatparam('-r', '5')
        strFilter = 'fps=5,scale=560:-1:flags=lanczos,palettegen'
        self.output.add_formatparam('-filter_complex', strFilter)

    def paletteuse(self, file):
        # Input
        self.input.add_formatparam('-i', '"'+file+'"')
        # Output
        self.output.add_formatparam('-r', '5')
        strFilter = '[1:v]fps=5,scale=560:-1:flags=lanczos[x];[x][0:v]paletteuse'
        self.output.add_formatparam('-filter_complex', strFilter)

    def videoSharp(self, luma=1, chroma=0):
        # Output
        strFilter = 'unsharp=la=%s:ca=%s' % (luma, chroma)
        self.output.add_formatparam('-filter_complex', strFilter)

    def transVideoRate(self, rate):
        # Output
        self.output.add_formatparam('-b', rate)
        self.output.add_formatparam('-movflags', 'faststart')

    """
    Other Handle
    """
    def run(self):
        self.output.overwrite()
        # FFmpeg(sys.path[0]+'/bin/ffmpeg.exe', self.input, self.output).run()
        return FFmpeg('ffmpeg.exe', self.input, self.output).run()

    def run_yb(self):
        self.output.overwrite()
        #获取当前工作目录
        currPath = os.getcwd()
        #更改当前工作目录
        os.chdir(os.path.join(currPath, 'bin_yb'))
        # FFmpeg(sys.path[0]+'/bin/ffmpeg.exe', self.input, self.output).run()
        result = FFmpeg(os.path.join(os.path.abspath('.'), 'ffmpeg.exe'), self.input, self.output).run()
        os.chdir(currPath)
        return result


if __name__ == '__main__':
    main()