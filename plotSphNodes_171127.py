import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pylab import rcParams

'''
v0.2 Dec. 02, 2017
    - plotSphNodes() takes [elevation] and [azimuth] args
v0.1 Nov. 27, 2017
    - add plotSphNodes()
'''

# on Matplotlib


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
    xx, yy, zz = np.hsplit(data, 3)

    # Plots in the hidden side are removed
    # since the code will display hidden plots
    xs, ys, zs = [], [], []
    for ax, ay, az in zip(xx, yy, zz):
        if (ax > 0):
            xs += [ax]
            ys += [ay]
            zs += [az]
    xx, yy, zz = xs, ys, zs

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
