#!/usr/bin/env python2

import re
import sys

import contour_util
import gcoder
import opti

import cv2

def write_gcode(filenum, width, height, contours):
    g = gcoder.GCoder()
    g.input_bounds(0, width, height, 0)
    g.add_lines(contours)

    out_w = 210.0 # A4
    out_h = out_w / width * height
    g.bounds(out_h/2, out_w/2, -out_h/2, -out_w/2)

    # Matt's
    #g.bounds(19, 19, -19, -19)
    g.tool_dia = 63.662
    g.write('images/camart-{:04d}.opti-M.ngc'.format(filenum))

    # Neil's
    #g.bounds(20, 17, -20, -17)
    g.tool_dia = 20
    g.write('images/camart-{:04d}.opti-N.ngc'.format(filenum))


def main():
    mainWindow = 'Leonerdo'
    filename = sys.argv[1]
    filenum=int(re.findall(r'-(\d\d\d\d).', filename)[0])

    contours = contour_util.read_contours(filename)

    contours_opti = opti.tsp(contours)

    moves = contour_util.moves(contours)
    moves_opti = contour_util.moves(contours_opti)

    img = cv2.imread('images/camart-{:04d}.jpg'.format(filenum))
    width = img.shape[1]
    height = img.shape[0]
    before = img.copy()
    vis_e = img.copy()

    contour_util.write_contours('images/camart-{:04d}.opti.contour'.format(filenum), contours_opti)

    write_gcode(filenum, width, height, contours_opti)

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
