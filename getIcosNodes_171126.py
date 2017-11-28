import numpy as np
from scipy.spatial import Delaunay
import freeBoundary_171112 as frb
import trisectTri_171125 as tst
import bisectTri_171123 as bst

'''
v0.2 Nov. 29, 2017
  - add Test_getIcosNodes()
v0.1 Nov. 26, 2017
  - add getIcosNodes()
'''


def getIcosNodes(kIndex, typeIndex):
    # Here are the nodes for the base icosahedron
    pos = (1 + np.sqrt(5.0)) / 2.0
    xs = [
        [0, pos, 1], [0, -pos, 1], [0, pos, -1],
        [0, -pos, -1], [1, 0, pos],
        [-1, 0, pos], [1, 0, -pos], [-1, 0, -pos],
        [pos, 1, 0], [-pos, 1, 0],
        [pos, -1, 0], [-pos, -1, 0],
    ]
    xs = np.array(xs)
    # Scale nodes so that they are on the surface of the sphere.
    x_l2 = []
    for elem in xs:
        x_l2 += [np.sqrt(np.sum(elem*elem))]
    x_l2 = np.array(x_l2)
    # ---reshape for [xs / x_l2]
    x_l2 = np.repeat(x_l2, len(xs[0]), axis=0)
    x_l2 = x_l2.reshape(len(xs), len(xs[0]))
    xs = xs / x_l2

    # Triangulate the points
    tris = Delaunay(xs).simplices
    tris = frb.find_freeBoundary(tris)

    if typeIndex == 0 and kIndex == 0:
        return xs, tris

    if typeIndex == 1:
        [xs, tris] = tst.trisectTri(xs, tris)
        if kIndex == 0:
            return xs, tris

    # Now just bisect the triangles.
    for loop in range(kIndex):
        xs, tris = bst.bisectTri(xs, tris)

    return xs, tris


def Test_getIcosNodes():
    resxs, restris = getIcosNodes(4, 0)
    print('---len')
    print(len(resxs), len(restris))
    print('---values')
    print(resxs)
    print(restris)
    '''
    ---len
    2562 5120
    ---values
    [[ 0.          0.85065081  0.52573111]
     [ 0.         -0.85065081  0.52573111]
     [ 0.          0.85065081 -0.52573111]
     ...,
     [ 0.99691733  0.04124839  0.06674129]
     [ 0.99760686 -0.06914159  0.        ]
     [ 0.99760686  0.06914159  0.        ]]
    [[   2 1624 1654]
     [   3 1578 1618]
     [   7 1116 1146]
     ...,
     [1087 1023 1043]
     [1042 1086 1022]
     [ 700  698  722]]
     '''
    pass  # for break point in [pdb]


if __name__ == '__main__':
    Test_getIcosNodes()
