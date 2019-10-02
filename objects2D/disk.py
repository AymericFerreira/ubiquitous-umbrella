import random
import numpy as np
from visual.visual import plot_points, plot_2D_points


def coordinate_in_disk(radius, points):
    pointList = []
    for loop in range(points):
        r = random.uniform(0, radius)
        theta = random.uniform(0, 2*np.pi)

        x = np.sqrt(r) * np.cos(theta)
        y = np.sqrt(r) * np.sin(theta)

        pointList.append([x, y])

    return np.array(pointList)


def quick_coordinate_in_disk(radius):
    r = random.uniform(0, radius)
    theta = random.uniform(0, 2 * np.pi)

    x = np.sqrt(r) * np.cos(theta)
    y = np.sqrt(r) * np.sin(theta)
    return x, y


def coordinate_on_disk(radius, points):
    pointList = []
    for loop in range(points):
        theta = random.uniform(0, 2*np.pi)

        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        pointList.append([x, y])

    return np.array(pointList)


def quick_coordinate_on_disk(radius):
    theta = random.uniform(0, 2 * np.pi)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y


if __name__ == "__main__":
    a = coordinate_on_disk(1, 1000)
    plot_2D_points(a)