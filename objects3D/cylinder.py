import random
import numpy as np
from visual.visual import plot_points, plot_2D_points, check_uniformity
import time
from objects2D.disk import quick_coordinate_in_disk, quick_coordinate_on_disk
import scipy.stats


def coordinate_in_cylinder(length, radius, points):
    pointList = []
    for loop in range(points):
        x, y = quick_coordinate_in_disk(radius)
        z = random.uniform(0, length)
        pointList.append([x, y, z])

    return np.array(pointList)


def coordinate_on_cylinder(length, radius, points):
    pointList = []
    for loop in range(points):
        x, y = quick_coordinate_on_disk(radius)
        z = random.uniform(0, length)
        pointList.append([x, y, z])

    return np.array(pointList)


if __name__ == "__main__":
    start = time.time()
    point1 = coordinate_on_cylinder(1, 10, 1000)
    # print(scipy.stats.chisquare(point1, axis=None))

    check_uniformity(point1)
    plot_points(point1)
    end = time.time()
    print(end - start)
    point2 = coordinate_in_cylinder(1, 1, 1000)
    end2 = time.time()
    print(end2 - end)
    # start = time.time()
    # a = coordinate_on_cylinder(1, 1, 1000)
    # end = time.time()
    # plot_points(a)
    # print(end - start)
    #
    # coordinate_in_cylinder(1, 1, 1000)
    # end = time.time()
    # print(end - start)