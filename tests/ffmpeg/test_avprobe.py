# -*-coding:utf8-*-#
import os
import pytest
import tempfile

from ffman.ffmpeg.avprob import AVProb

def test_getVideoLen():
    ffprobe = AVProb("./tests/data/input.mp4")
    videoLen = ffprobe.getVideoLen()
    assert videoLen == 3.52

def test_getVideoSize():
    ffprobe = AVProb("./tests/data/input.mp4")
    size = ffprobe.getVideoSize()
    assert size == 340825

def test_getVideoWidth():
    ffprobe = AVProb("./tests/data/input.mp4")
    width = ffprobe.getVideoWidth()
    assert width == 1920

def test_getVideoHeight():
    ffprobe = AVProb("./tests/data/input.mp4")
    height = ffprobe.getVideoHeight()
    assert height == 1080

def test_getVideoFrameRate():
    ffprobe = AVProb("./tests/data/input.mp4")
    frameRate = ffprobe.getVideoFrameRate()
    assert frameRate == 25

def test_getVideoFrames():
    ffprobe = AVProb("./tests/data/input.mp4")
    frames = ffprobe.getVideoFrames()
    assert frames == 88

if __name__ == "__main__":
    pytest.main()