import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_points(pointlist):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # for point in pointlist:
    #     ax.scatter(point[0], point[1], point[2])

    ax.scatter(pointlist[:, 0], pointlist[:, 1], pointlist[:, 2])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def plot_2D_points(pointlist):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # for point in pointlist:
    #     ax.scatter(point[0], point[1])
    ax.scatter(pointlist[:, 0], pointlist[:, 1])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    plt.show()


def check_uniformity(pointlist):
    fig = plt.figure()
    ax = fig.add_subplot(221)
    ax.scatter(pointlist[:, 0], pointlist[:, 1])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    ax = fig.add_subplot(222)
    ax.scatter(pointlist[:, 0], pointlist[:, 2])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Z Label')

    ax = fig.add_subplot(223)
    ax.scatter(pointlist[:, 1], pointlist[:, 2])

    ax.set_xlabel('Y Label')
    ax.set_ylabel('Z Label')

    ax = fig.add_subplot(224, projection='3d')
    ax.scatter(pointlist[:, 0], pointlist[:, 1], pointlist[:, 2])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()