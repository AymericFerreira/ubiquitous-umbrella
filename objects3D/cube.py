import random
import numpy as np
from visual.visual import plot_points, plot_2D_points, check_uniformity
import time


def coordinate_in_cube(length, points):
    pointList = []
    for loop in range(points):
        demiLength = length/2
        x = random.uniform(-demiLength, demiLength)
        y = random.uniform(-demiLength, demiLength)
        z = random.uniform(-demiLength, demiLength)
        pointList.append([x, y, z])

    return np.array(pointList)


def coordinate_on_cube(length, points):
    pointList = []
    for loop in range(points):
        demiLength = length / 2

        fixAxis = random.randint(1, 6)

        if fixAxis == 1:
            x = random.uniform(-demiLength, demiLength)
            y = random.uniform(-demiLength, demiLength)
            z = demiLength
        elif fixAxis == 2:
            x = random.uniform(-demiLength, demiLength)
            y = demiLength
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 3:
            x = demiLength
            y = random.uniform(-demiLength, demiLength)
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 4:
            x = random.uniform(-demiLength, demiLength)
            y = random.uniform(-demiLength, demiLength)
            z = -demiLength
        elif fixAxis == 5:
            x = random.uniform(-demiLength, demiLength)
            y = -demiLength
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 6:
            x = -demiLength
            y = random.uniform(-demiLength, demiLength)
            z = random.uniform(-demiLength, demiLength)

        pointList.append([x, y, z])

    return np.array(pointList)


if __name__ == "__main__":
    start = time.time()
    a = coordinate_in_cube(1, 1000)
    check_uniformity(a)
