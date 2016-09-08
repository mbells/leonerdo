#!/usr/bin/env python2

import re
import sys

import contour_util
import gcoder
import opti

import cv2
#import video


def main():
    mainWindow = 'Leonerdo'
    filename = sys.argv[1]
    filenum=int(re.findall(r'-(\d\d\d\d).', filename)[0])

    contours = contour_util.read_contours(filename)

    contours_opti = opti.tsp(contours)

    moves = contour_util.moves(contours)
    moves_opti = contour_util.moves(contours_opti)

    fn = 0
    img = cv2.imread('images/camart-{:04d}.jpg'.format(filenum)) #video.create_capture(fn)
    width = img.shape[1]
    height = img.shape[0]
    before = img.copy()
    vis_e = img.copy()

    contour_util.write_contours('images/camart-{:04d}.opti.contour'.format(filenum), contours_opti)

    g = gcoder.GCoder()
    g.input_bounds(0, width, height, 0)
    g.add_lines(contours_opti)
    g.write('images/camart-{:04d}.opti.ngc'.format(filenum))

    while True:
        cv2.drawContours(before, moves, -1, (0,0,255), 1)
        cv2.drawContours(before, contours, -1, (0,255,0), 2)
        cv2.imshow('before', before)

        cv2.drawContours(vis_e, moves_opti, -1, (0,0,255), 1)
        cv2.drawContours(vis_e, contours_opti, -1, (0,255,0), 2)
        cv2.imshow('after', vis_e)

        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
