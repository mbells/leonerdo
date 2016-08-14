
import numpy as np
import sys

def moves(contours):
    result = []
    prev = contours[0]
    for contour in contours[1:]:
        start = prev[-1]
        end = contour[0]
        contour = [start, end]
        result.append(numpy_contour(contour))
        prev = contour
    return result

def numpy_contour(contour):
    #c1 = np.array(contour)
    npc = np.ndarray(shape=(len(contour), 1, 2), dtype=np.int32, buffer=None)
    for i in range(len(contour)):
        npc[i][0][0] = contour[i][0][0]
        npc[i][0][1] = contour[i][0][1]
    return npc


def read_contours(filename):
    contour = None
    contours=[]
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line == '-\n':
                if contour is not None:
                    contours.append(numpy_contour(contour))
                contour = []
            else:
                values = line.split(',')
                point = [[int(values[0]), int(values[1])]]
                contour.append(point)
    contours.append(numpy_contour(contour))
    return contours


def write_contours(filename, contours):
    with open(filename, 'w') as f:
        for contour in contours:
            f.write('-\n')
            for point in contour:
                point = point[0]
                f.write(str(point[0]) + ',' + str(point[1]) + '\n')


