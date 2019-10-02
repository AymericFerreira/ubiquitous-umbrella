import random
import numpy as np
from visual.visual import plot_points, plot_2D_points


def coordinate_in_triangle(base, edge1length, edge2length, points):
    pointList = []
    for loop in range(points):
        r = random.uniform(0, 1)
        s = random.uniform(0, 1)

        if r+s >= 1:
            r = 1-r
            s = 1-s

        x, y = base[0] + r * edge1length, base[1] + s * edge2length
        pointList.append([x, y])

    return np.array(pointList)


def coordinate_in_triangle_position(point1, point2, point3, points):
    pointList = []
    for loop in range(points):
        r = random.uniform(0, 1)
        s = random.uniform(0, 1)

        if r + s >= 1:
            r = 1 - r
            s = 1 - s

        x, y = point1[0] + r * (point2[0]-point1[0]), point1[1] + s * (point3[1] - point1[1])
        pointList.append([x, y])

    return np.array(pointList)


if __name__ == '__main__':
    # a = coordinate_in_triangle([0, 0], 1, 1, 1000)
    a = coordinate_in_triangle_position([0, 0], [1, 0], [1, 1], 1000)
    plot_2D_points(a)
