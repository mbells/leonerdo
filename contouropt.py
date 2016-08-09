#!/usr/bin/env python2

import sys

import contour_util

import cv2
import video


def main():
    mainWindow = 'Leonerdo'
    filename = sys.argv[1]
    contours = contour_util.read_contours(filename)
    #print(contours)

    fn = 0
    cap = video.create_capture(fn)
    flag, img = cap.read()
    vis_e = img.copy()

    while True:
        cv2.drawContours(vis_e, contours, -1, (0,255,0), 2)
        cv2.imshow(mainWindow, vis_e)
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
