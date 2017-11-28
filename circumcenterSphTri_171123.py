import numpy as np
import sys

'''
v0.2 Nov. 23, 2017
  - add test_circumcenterSphTri()
v0.1 Nov. 23, 2017
  - add calc_xc()
  - add calc_gamma()
  - add calc_beta()
  - add calc_denom()
  - add calc_alpha()
  - add calc_dotProduct_2d()
  - add calc_verticesDistance()
  - add circumcenterSphTri()
'''


def calc_dotProduct(x1, x2):
    ndim = x1.ndim
    if ndim == 1:
        return np.sum(np.dot(x1, x2))

    res = []
    for idx in range(ndim):
        res += [np.dot(x1[idx], x2[idx])]
    return np.array(res)


def calc_verticesDistance(xs, ys, zs, tris, idx0, idx1):
    tri0 = tris[:, idx0]
    tri1 = tris[:, idx1]

    res = []
    for pos0, pos1 in zip(tri0, tri1):
        wrk = xs[pos0] * xs[pos1]
        wrk += ys[pos0] * ys[pos1]
        wrk += zs[pos0] * zs[pos1]
        res += [2.0 * (1.0 - wrk)]
    return res


def calc_denom(tris, nodes):
    # 1. calc cross
    lhs = []
    rhs = []
    for pos0, pos1, pos2 in zip(tris[:, 0], tris[:, 1], tris[:, 2]):
        lhs += [nodes[pos0, :] - nodes[pos1, :]]
        rhs += [nodes[pos0, :] - nodes[pos2, :]]
    crs = np.cross(lhs, rhs)

    # 2. calc denom
    res = []
    for elem in np.array(crs*crs):
        wrk = np.sum(elem)
        res += [2.0*wrk]
    return res


def calc_alpha(tris, nodes, rd2):
    dpt = []
    for pos0, pos1, pos2 in zip(tris[:, 0], tris[:, 1], tris[:, 2]):
        lhs = nodes[pos0, :] - nodes[pos1, :]
        rhs = nodes[pos0, :] - nodes[pos2, :]
        dpt += [calc_dotProduct(lhs, rhs)]
    res = rd2[1] * dpt
    return res


def calc_beta(tris, nodes, rd2):
    dpt = []
    for pos0, pos1, pos2 in zip(tris[:, 0], tris[:, 1], tris[:, 2]):
        lhs = nodes[pos1, :] - nodes[pos0, :]
        rhs = nodes[pos1, :] - nodes[pos2, :]
        dpt += [calc_dotProduct(lhs, rhs)]
    return rd2[2] * dpt


def calc_gamma(tris, nodes, rd2):
    dpt = []
    for pos0, pos1, pos2 in zip(tris[:, 0], tris[:, 1], tris[:, 2]):
        lhs = nodes[pos2, :] - nodes[pos0, :]
        rhs = nodes[pos2, :] - nodes[pos1, :]
        dpt += [calc_dotProduct(lhs, rhs)]
    return rd2[0] * dpt


def calc_xc(alpha, beta, gamma, tris, nodes):
    res = []
    for aalp, abet, agam, pos0, pos1, pos2 in zip(
            alpha, beta, gamma,
            tris[:, 0], tris[:, 1], tris[:, 2]
            ):
        xc = np.tile(aalp, (1, 3)) * nodes[pos0, :]
        xc += np.tile(abet, (1, 3)) * nodes[pos1, :]
        xc += np.tile(agam, (1, 3)) * nodes[pos2, :]
        res += [*xc]
    res = np.array(res)
    return res


def circumcenterSphTri(tris, nodes):
    xs = nodes[:, 0]
    ys = nodes[:, 1]
    zs = nodes[:, 2]
    rd2 = [calc_verticesDistance(xs, ys, zs, tris, idx0=0, idx1=1)]
    rd2 += [calc_verticesDistance(xs, ys, zs, tris, idx0=1, idx1=2)]
    rd2 += [calc_verticesDistance(xs, ys, zs, tris, idx0=0, idx1=2)]
    rd2 = np.array(rd2)

    alpha = calc_alpha(tris, nodes, rd2)
    denom = calc_denom(tris, nodes)
    alpha = alpha / denom
    beta = calc_beta(tris, nodes, rd2)
    beta = beta / denom
    gamma = calc_gamma(tris, nodes, rd2)
    gamma = gamma / denom
    xc = calc_xc(alpha, beta, gamma, tris, nodes)

    # Project onto the sphere.
    x_l2 = []
    for elem in xc:
        x_l2 += [np.sqrt(np.sum(elem*elem))]
    x_l2 = np.array(x_l2)
    # ---reshape for [xc / x_l2]
    x_l2 = np.repeat(x_l2, len(xc[0]), axis=0)
    x_l2 = x_l2.reshape(len(xc), len(xc[0]))

    xc = xc / x_l2
    return xc


def test_circumcenterSphTri_171123():
    # [x0, tri0] = getIcosNodes(4,1)

    ans = [[-0.57735027,  0.57735027,  0.57735027],
           [-0.35682209,  0.93417236,  0.],
           [0.57735027, -0.57735027,  0.57735027],
           [-0.93417236,  0.,  0.35682209],
           [-0.93417236,  0., -0.35682209],
           [-0.57735027, -0.57735027, -0.57735027],
           [-0.57735027,  0.57735027, -0.57735027],
           [0.,  0.35682209,  0.93417236],
           [0., -0.35682209,  0.93417236],
           [0.35682209,  0.93417236,  0.],
           [0.57735027,  0.57735027,  0.57735027],
           [0.93417236,  0.,  0.35682209],
           [-0.35682209, -0.93417236,  0.],
           [-0.57735027, -0.57735027,  0.57735027],
           [0.,  0.35682209, -0.93417236],
           [0., -0.35682209, -0.93417236],
           [0.57735027, -0.57735027, -0.57735027],
           [0.35682209, -0.93417236,  0.],
           [0.93417236,  0., -0.35682209],
           [0.57735027,  0.57735027, -0.57735027]]
    ans = np.array(ans)

    tris = [
            [10, 6,    1],
            [3, 10,    1],
            [11, 5,    2],
            [12, 6,   10],
            [8, 12,   10],
            [4, 12,    8],
            [8, 10,    3],
            [5,  1,    6],
            [5,  6,    2],
            [3,  1,    9],
            [5,  9,    1],
            [11, 9,    5],
            [12, 4,    2],
            [6, 12,    2],
            [8,  3,    7],
            [8,  7,    4],
            [11, 4,    7],
            [11, 2,    4],
            [7,  9,   11],
            [3,  9,    7],
        ]

    nodes = [
      [0.0000000e+00,  8.5065081e-01,  5.2573111e-01],
      [0.0000000e+00, -8.5065081e-01,  5.2573111e-01],
      [0.0000000e+00,  8.5065081e-01, -5.2573111e-01],
      [0.0000000e+00, -8.5065081e-01, -5.2573111e-01],
      [5.2573111e-01,  0.0000000e+00,  8.5065081e-01],
      [-5.2573111e-01,  0.0000000e+00,  8.5065081e-01],
      [5.2573111e-01,  0.0000000e+00, -8.5065081e-01],
      [-5.2573111e-01,  0.0000000e+00, -8.5065081e-01],
      [8.5065081e-01,  5.2573111e-01,  0.0000000e+00],
      [-8.5065081e-01,  5.2573111e-01,  0.0000000e+00],
      [8.5065081e-01, -5.2573111e-01,  0.0000000e+00],
      [-8.5065081e-01, -5.2573111e-01,  0.0000000e+00],
    ]

    tris = np.array(tris)
    tris = tris - 1  # from indexing [1..] to [0..]
    nodes = np.array(nodes)
    res = circumcenterSphTri(tris, nodes)
    print("---res")
    print(res)
    print("---answer")
    print(ans)


if __name__ == '__main__':
    test_circumcenterSphTri_171123()
