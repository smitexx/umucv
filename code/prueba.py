#!/usr/bin/env python

# > ./stream.py
# > ./stream.py --dev=help

import cv2          as cv
from umucv.stream import autoStream
from umucv.util import Video
import numpy as np

video = Video()
for key,frame in autoStream():
    if key != 255:
        print(key)
    result = frame[:200, 300:, 0]
    invert = np.rot90(255-result)
    cv.imshow('input',frame)
    cv.imshow('resultado', result)
    cv.imshow('inversion', invert)

    video.write(invert, key, ord('v'))
cv.destroyAllWindows()
video.release()

