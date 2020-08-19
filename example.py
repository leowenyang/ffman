from ffman.ffmpeg.avimage import AVImage

def testColorBar():
    outFile = "./tests/data/colorBar.mp4"
    avImage = AVImage("./tests/data/input.mp4", outFile)
    avImage.colorBar(1, 1, 1000, 100, '#FF0000@0.5')
    avImage.run()

if __name__ == "__main__":
    testColorBar()