import random
import numpy as np
import time

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

    return pointList

def coordinate_in_sphere_volume(radius, points):
    pointList = []
    for loop in range(points):
        rs = random.uniform(0, radius)

        theta = random.uniform(0, 2 * np.pi)
        phi = random.uniform(0, np.pi)

        x = rs * np.sin(theta) * np.cos(phi)
        y = rs * np.sin(theta) * np.sin(phi)
        z = rs * np.cos(theta)

        pointList.append([x, y, z])

    return pointList

def coordinate_on_sphere_surface_archimede(radius, points):
    pointList = []
    for loop in range(points):
        rs = radius

        z = random.uniform(-rs, rs)
        theta = random.uniform(0, 2 * np.pi)

        x = np.sqrt(rs * rs - z * z) * np.cos(theta)
        y = np.sqrt(rs * rs - z * z) * np.sin(theta)

        pointList.append([x, y, z])

    return pointList

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

    return pointList

def coordinate_on_sphere_surface_cube(radius, points):
    pointList = []
    loop = 0
    while loop < points:
        rs = radius

        x = random.uniform(-rs, rs)
        y = random.uniform(-rs, rs)
        z = random.uniform(-rs, rs)

        if x * x + y * y + z * z == rs * rs:
            loop += 1
            pointList.append([x, y, z])

    return pointList


if __name__ == "__main__":
    start = time.time()
    coordinate_on_sphere_surface(1, 10000)
    print(f'1 : {time.time()-start}')
    coordinate_in_sphere_volume(1, 10000)
    print(f'2 : {time.time() - start}')
    coordinate_on_sphere_surface_archimede(1, 10000)
    print(f'3 : {time.time() - start}')
    coordinate_in_sphere_volume_cube(1, 10000)
    print(f'4 : {time.time() - start}')
    # coordinate_on_sphere_surface_cube(1, 1000)
    # print(f'5 : {time.time() - start}')
