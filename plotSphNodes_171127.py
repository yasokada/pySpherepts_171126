import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pylab import rcParams
import sys

'''
v0.3 Dec. 03, 2017
    - add extractFrontPoints()
v0.2 Dec. 02, 2017
    - plotSphNodes() takes [elevation] and [azimuth] args
v0.1 Nov. 27, 2017
    - add plotSphNodes()
'''

# on Matplotlib

def extractFrontPoints(data, elevation, azimuth):
    xx, yy, zz = np.hsplit(data, 3)

    # 1. prepare the rotation matrix
    theta = np.radians(elevation)
    phi = np.radians(azimuth)
    # 1-1. rotation for theta around the y axis
    rottht = [
        [np.cos(theta), 0.0, np.sin(theta)],
        [0.0, 1.0, 0.0],
        [-np.sin(theta), 0.0, np.cos(theta)],
    ]
    # 1-2. rotation for phi around the z axis
    rotphi = [
        [np.cos(-phi), -np.sin(-phi), 0.0],
        [np.sin(-phi), np.cos(-phi), 0.0],
        [0.0, 0.0, 1.0],
    ]

    # 2. Plots in the hidden side are removed
    #   since the code will display hidden plots
    xs, ys, zs = [], [], []
    for axo, ayo, azo in zip(xx, yy, zz):
        # 2-1. rotatio in theta and phi
        #   **rotate in theta firstly will fail**
        wrk = np.matmul(rotphi, [axo, ayo, azo])
        axr, ayr, azr = np.matmul(rottht, wrk)

        # 2-2. extract only front points
        if (axr > 0):
            xs += [axo]
            ys += [ayo]
            zs += [azo]
    xx, yy, zz = xs, ys, zs

    return xx, yy, zz


def plotSphNodes(data, elevation=0.0, azimuth=0.0):
    # Create a sphere
    r = 1
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)

    data = data * 1.0005
    xx, yy, zz = extractFrontPoints(data, elevation, azimuth)

    # Set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # a single big sphere in the center
    ax.plot_surface(
        x, y, z,  rstride=1, cstride=1,
        color='y', alpha=1.0, linewidth=0, shade=False)

    # plots over the big sphere
    ax.scatter(xx, yy, zz, color="k", s=15)

    # other settings
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect("equal")
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.tight_layout()
    # elevation and azimuth
    # where azimuth is [MATLAB's azimuth - 90] degrees
    ax.view_init(elev=elevation, azim=azimuth)
    plt.show()
