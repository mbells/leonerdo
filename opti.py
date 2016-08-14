'''
Collection of optimization functions for contours.
'''

import math
import numpy as np

from tsp_solver.greedy_numpy import solve_tsp

def contour_len(contour):
    result = 0

    pa = contour[0]
    for pb in contour[1:]:
        result += distance_euclidean(pa[0], pb[0])
        pa = pb
    return result


def distance_euclidean(point_a, point_b):
    return math.sqrt((point_b[0]-point_a[0])**2 + (point_b[1]-point_a[1])**2)


def filter_small_contours(contours):
    result = []
    for contour in contours:
        if contour_len(contour) > 40:
            result.append(contour)
    return result

def reverse(contour):
    npc = np.ndarray(shape=(len(contour), 1, 2), dtype=np.int32, buffer=None)
    n = len(contour)
    for i in range(n):
        npc[i][0][0] = contour[n-i-1][0][0]
        npc[i][0][1] = contour[n-i-1][0][1]
    return npc

class TspGraph:
    def __init__(self, contours, points):
        self.contours = contours
        self.points = points
        self.matrix = []

    def contours_from_path(self, path):
        result = []

        for i in range(0, len(path), 2):
            p1 = path[i]
            p2 = path[i+1]

            if self.points_adjacent(p1, p2):
                contour = self.contours[p1/2]
                if self.is_reversed(p1, p2):
                    contour = reverse(contour)
                result.append(contour)
            else:
                if p1 % 2 == 0:
                    contour = self.contours[p1/2]
                    result.append(contour)
                if p2 % 2 == 0:
                    contour = self.contours[p2/2]
                    result.append(contour)
        return result

    def distance(self, p1, p2):
        if self.points_adjacent(p1, p2):
            return 0
        else:
            return distance_euclidean(self.points[p1], self.points[p2])

    def get_matrix(self):
        size = len(self.points)
        self.matrix = [[0 for x in range(len(self.points))] for y in range(len(self.points))]
        for from_node in range(size):
            for to_node in range(size):
                if from_node == to_node:
                    self.matrix[from_node][to_node] = 0
                else:
                    self.matrix[from_node][to_node] = self.distance(from_node, to_node)
        return self.matrix

    def is_reversed(self, p1, p2):
        return p2 +1 == p1 and p2 % 2 == 0

    def points_adjacent(self, p1, p2):
        return (p1 +1 == p2 and p1 % 2 == 0) or (p2 +1 == p1 and p2 % 2 == 0)



def ordered(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def tsp(contours):
    tsp = tsp_from_contours(contours)
    print(len(contours))
    m = tsp.get_matrix()
    path = solve_tsp(m)
    return tsp.contours_from_path(path)


def tsp_from_contours(contours):
    points = []
    i = 0
    for contour in contours:
        first = contour[0][0]
        last = contour[-1][0]
        points.append(first)
        points.append(last)

        i += 1

    tsp = TspGraph(contours, points)
    return tsp
