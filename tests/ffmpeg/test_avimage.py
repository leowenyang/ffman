# -*-coding:utf8-*-#
import os
import pytest
import tempfile

from ffman.ffmpeg.avimage import AVImage

def test_colorBar():
    outFile = "./tests/data/colorBar.mp4"
    avImage = AVImage("./tests/data/input.mp4", outFile)
    avImage.colorBar(1, 1, 1000, 20, '#FF0000')
    avImage.run()

    assert os.path.exists(outFile)
    os.remove(outFile)  

# def test_colorMove():
#     outFile = "./tests/data/output.mp4"
#     avImage = AVImage("./tests/data/input.mp4", outFile)
#     frames = avImage.colorMove()
#     assert frames == 88

if __name__ == "__main__":
    pytest.main()