import random
import numpy as np
import time
from visual.visual import plot_points, plot_2D_points
import scipy.stats


def coordinate_on_sphere_surface(radius, points):
    pointList = []
    # pointList = np.zeros((points))
    for loop in range(points):
        rs = radius

        theta = random.uniform(0, 2 * np.pi)
        phi = random.uniform(0, np.pi)

        x = rs * np.sin(theta) * np.cos(phi)
        y = rs * np.sin(theta) * np.sin(phi)
        z = rs * np.cos(theta)

        pointList.append([x, y, z])
        # pointList[loop].append([x, y, z])

    return np.array(pointList)


def coordinate_in_sphere_volume(radius, points):
    pointList = []
    for loop in range(points):
        # rs = np.sqrt(random.uniform(0, 1)) * radius
        rs = random.uniform(0, radius)

        theta = random.uniform(0, 2 * np.pi)
        phi = random.uniform(0, np.pi)

        x = rs * np.sin(theta) * np.cos(phi)
        y = rs * np.sin(theta) * np.sin(phi)
        z = rs * np.cos(theta)

        pointList.append([x, y, z])

    return np.array(pointList)


def coordinate_in_sphere_volume_(radius, points):
    pointList = []
    for loop in range(points):
        # rs = np.sqrt(random.uniform(0, 1)) * radius
        rs = np.cbrt(random.uniform(0, radius))

        theta = random.uniform(0, 2 * np.pi)
        phi = random.uniform(0, np.pi)

        x = rs * np.sin(phi) * np.cos(theta)
        y = rs * np.sin(phi) * np.sin(theta)
        z = rs * np.cos(phi)

        pointList.append([x, y, z])

    return np.array(pointList)


def coordinate_on_sphere_surface_archimede(radius, points):
    pointList = []
    for loop in range(points):
        rs = radius

        z = random.uniform(-rs, rs)
        theta = random.uniform(0, 2 * np.pi)

        x = np.sqrt(rs * rs - z * z) * np.cos(theta)
        y = np.sqrt(rs * rs - z * z) * np.sin(theta)

        pointList.append([x, y, z])

    return np.array(pointList)


def coordinate_in_sphere_volume_cube(radius, points):
    pointList = []
    loop = 0
    while loop < points:
        rs = radius

        x = random.uniform(-rs, rs)
        y = random.uniform(-rs, rs)
        z = random.uniform(-rs, rs)

        if x * x + y * y + z * z <= rs * rs:
            loop += 1
            pointList.append([x, y, z])

    return np.array(pointList)

# Too long to compute

# def coordinate_on_sphere_surface_cube(radius, points):
#     pointList = []
#     loop = 0
#     while loop < points:
#         rs = radius
#
#         x = random.uniform(-rs, rs)
#         y = random.uniform(-rs, rs)
#         z = random.uniform(-rs, rs)
#
#         if x * x + y * y + z * z == rs * rs:
#             loop += 1
#             pointList.append([x, y, z])
#
#     return pointList


if __name__ == "__main__":
    start = time.time()
    # a = coordinate_on_sphere_surface(10, 1000)
    # plot_2D_points(a)
    b = coordinate_in_sphere_volume(10, 1000)
    plot_2D_points(b)
    b = coordinate_in_sphere_volume_(10, 1000)
    plot_2D_points(b)
    # c = coordinate_on_sphere_surface_archimede(10, 1000)
    # plot_2D_points(c)
    d = coordinate_in_sphere_volume_cube(10, 1000)
    plot_2D_points(d)
    # plot_points(pointList1)
