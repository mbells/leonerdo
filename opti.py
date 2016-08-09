'''
Collection of optimization functions for contours.
'''

import math


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

class TspGraph:
    def __init__(self, points):
        self.points = points

    def points_adjacent(p1, p2):
        return (p1 +1 == p2 and p1 % 2 == 0) or (p2 +1 == p1 and p2 % 2 == 0)

    def distance(self, p1, p2):
        if points_adjacent(p1, p2):
            return 0
        else:
            return distance_euclidean(points[p1], points[p2])

    def matrix():
        size = len(self.points)
        for from_node in range(size):
            self.matrix[from_node] = {}
            for to_node in range(size):
                if from_node == to_node:
                    self.matrix[from_node][to_node] = 0
                else:
                    self.matrix[from_node][to_node] = self.distance(from_node, to_node)
        return self.matrix



def ordered(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def tsp(contours):
    tsp = tsp_from_contours(contours)
    m = tsp.matrix()


def tsp_from_contours(contours):
    points = []
    i = 0
    for contour in contours:
        first = contour[0]
        last = contour[-1]
        points.append(first)
        points.append(last)

        i += 1

    tsp = TspGraph(points)
    return tsp
