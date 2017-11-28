import numpy as np
import sys
import trisectEdge_171122 as tse
import circumcenterSphTri_171123 as ccs
import array_tool_171125 as art
from scipy.spatial import Delaunay
import freeBoundary_171112 as frb

'''
v0.3 Nov. 29, 2017
  - add Test_trisectTri()
v0.2 Nov. 26, 2017
  - use np.concatenate() instead of my own concatenating code
v0.1 Nov. 25, 2017
  - import [freeBoundary_171112]
  - use Delaunay()
  - add trisectTri()
'''


def trisectTri(xs, tris):
    tris = np.array(tris).astype(int)
    kidx = 0
    v1 = np.zeros((2*len(tris), 3))
    v2 = np.zeros((2*len(tris), 3))
    v3 = np.zeros((2*len(tris), 3))
    for jidx in range(len(tris)):
        tri0 = tris[jidx, 0]
        tri1 = tris[jidx, 1]
        tri2 = tris[jidx, 2]
        wrk = tse.trisectEdge(xs[tri0, :], xs[tri1, :])
        v1[kidx:kidx+2, :] = wrk.copy()
        wrk = tse.trisectEdge(xs[tri1, :], xs[tri2, :])
        v2[kidx:kidx+2, :] = wrk.copy()
        wrk = tse.trisectEdge(xs[tri2, :], xs[tri0, :])
        v3[kidx:kidx+2, :] = wrk.copy()

        kidx += 2

    vs = np.concatenate((v1, v2, v3), axis=0)

    # Add the circumcenter of the original triangle to the list.
    wrk = ccs.circumcenterSphTri(tris, xs)
    vs = np.concatenate((vs, wrk), axis=0)
    vs = np.concatenate((xs, vs), axis=0)

    # Remove repeating vertices
    xs, _ = art.get_unique_rows(vs)

    # Project the nodes to the sphere.
    x_l2 = []
    for elem in xs:
        x_l2 += [np.sqrt(np.sum(elem*elem))]
    x_l2 = np.array(x_l2)
    # ---reshape for [xs / x_l2]
    x_l2 = np.repeat(x_l2, len(xs[0]), axis=0)
    x_l2 = x_l2.reshape(len(xs), len(xs[0]))
    xs = xs / x_l2

    # Triangulate the new nodes;
    tris = Delaunay(xs).simplices
    tris = frb.find_freeBoundary(tris)

    tris = np.array(tris).astype(int)

    return xs, tris


def Test_trisectTri():
    tris = np.genfromtxt('tri_trisect_171125.txt', delimiter='  ')
    xs = np.genfromtxt('x_trisect_171125.txt', delimiter='  ')
    tris = tris.astype(int)  # file is in float
    tris = tris - 1  # from indexing [1..] to [0..]

    resxs, restris = trisectTri(xs, tris)
    '''
    (Pdb) p len(resxs)
    92
    (Pdb) p resxs[:5]
    array([[-0.98302355, -0.18347941,  0.        ],
           [-0.98302355,  0.18347941,  0.        ],
           [-0.93417236,  0.        , -0.35682209],
           [-0.93417236,  0.        ,  0.35682209],
           [-0.85198102, -0.39551069, -0.34307382]])
    (Pdb) p resxs[-5:]
    array([[ 0.85198102,  0.39551069,  0.34307382],
           [ 0.93417236,  0.        , -0.35682209],
           [ 0.93417236,  0.        ,  0.35682209],
           [ 0.98302355, -0.18347941,  0.        ],
           [ 0.98302355,  0.18347941,  0.        ]])

    (Pdb) p len(restris)
    180
    (Pdb) p restris[:5]
    array([[13, 27, 23],
           [ 4,  2, 10],
           [ 5,  3,  0],
           [33, 37, 49],
           [55, 59, 71]])
    (Pdb) p restris[-5:]
    array([[24, 34, 44],
           [22, 24, 10],
           [24, 18, 10],
           [53, 47, 39],
           [53, 65, 45]])
    '''
    # print(resxs)
    pass  # for breakpoint in pdb


if __name__ == '__main__':
    Test_trisectTri()
