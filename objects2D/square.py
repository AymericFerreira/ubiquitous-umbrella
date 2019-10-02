import random
import numpy as np
from visual.visual import plot_points, plot_2D_points, check_uniformity


def coordinate_in_square(length, points):
    pointList = []
    for loop in range(points):
        demiLength = length / 2

        x = random.uniform(-demiLength, demiLength)
        y = random.uniform(-demiLength, demiLength)

        pointList.append([x, y])

    return np.array(pointList)


def coordinate_on_square(length, points):
    pointList = []
    for loop in range(points):
        demiLength = length / 2

        fixAxis = random.randint(1, 4)

        if fixAxis == 1:
            x = random.uniform(-demiLength, demiLength)
            y = demiLength
        elif fixAxis == 2:
            x = random.uniform(-demiLength, demiLength)
            y = -demiLength
        elif fixAxis == 3:
            x = demiLength
            y = random.uniform(-demiLength, demiLength)
        elif fixAxis == 4:
            x = -demiLength
            y = random.uniform(-demiLength, demiLength)
        pointList.append([x, y])

    return np.array(pointList)


if __name__ == "__main__":
    a = coordinate_on_square(1, 1000)
    plot_2D_points(a)
