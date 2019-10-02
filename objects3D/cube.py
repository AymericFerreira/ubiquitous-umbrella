import random
import numpy as np
from visual.visual import plot_points, plot_2D_points
import time
import scipy.stats


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
        x = random.uniform(-demiLength, demiLength)
        y = random.uniform(-demiLength, demiLength)
        z = random.uniform(-demiLength, demiLength)
        x /= np.sqrt(x*x + y*y + z*z)
        y /= np.sqrt(x*x + y*y + z*z)
        z /= np.sqrt(x*x + y*y + z*z)
        pointList.append([x, y, z])

    return np.array(pointList)


if __name__ == "__main__":
    start = time.time()
    a = coordinate_in_cube(1, 1000)
    print(a)
    print(scipy.stats.ks_2samp(a[:,0], a[:,1]))
    print(scipy.stats.ks_2samp(a[:,1], a[:,2]))
    print(scipy.stats.ks_2samp(a[:,0], a[:,2]))
    end = time.time()
    plot_2D_points(a)
    z = np.random.random_sample(1000,)
    b = []
    for i in range(1000):
        b.append(random.uniform(0, 1))

    c = []
    for i in range(1000):
        c.append(random.gauss(0.5, 1))

    print(scipy.stats.kstest(np.transpose(z), 'uniform'))
    print(scipy.stats.kstest(np.transpose(z), 'norm'))

    print(scipy.stats.kstest(np.transpose(b), 'uniform'))
    print(scipy.stats.kstest(np.transpose(b), 'norm'))

    print(scipy.stats.kstest(np.transpose(c), 'uniform'))
    print(scipy.stats.kstest(np.transpose(c), 'norm'))

    print(scipy.stats.ks_2samp(b, b))
    print(scipy.stats.ks_2samp(b, c))
    print(scipy.stats.ks_2samp(b, z))
    print(scipy.stats.ks_2samp(c, z))

    print(scipy.stats.chisquare([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]))
    print(end - start)

    coordinate_in_cube(1, 1000)
    end = time.time()
    print(end - start)
