import numpy as np
import sys
import array_tool_171125 as art

'''
v0.4 Nov. 28, 2017
  - add Test_bisectTri()
v0.3 Nov. 26, 2017
  - use np.concatenate() instead of my own concatenating code
v0.2 Nov. 25, 2017
  - move get_unique_rows() to [array_tool_171125]
v0.1 Nov. 24, 2017
  - add bisectTri()
  - add add_to_array_vertical()
  - add get_unique_rows()
'''


def add_to_array_vertical(vlist):
    ret = np.transpose(vlist).reshape(len(vlist[0]), len(vlist))
    return ret


def bisectTri(xs, tris):
    tris = np.array(tris).astype(int)
    # Number of vertices
    Nx = len(xs)
    # Number of triangles
    Nt = len(tris)

    # Bisect each edge
    v1, v2, v3 = [], [], []
    for pos0, pos1, pos2 in zip(tris[:, 0], tris[:, 1], tris[:, 2]):
        v1 += [(xs[pos0, :] + xs[pos1, :]) / 2]
        v2 += [(xs[pos1, :] + xs[pos2, :]) / 2]
        v3 += [(xs[pos2, :] + xs[pos0, :]) / 2]
    v1, v2, v3 = np.array(v1), np.array(v2), np.array(v3)
    vs = np.concatenate((v1, v2, v3), axis=0)

    # Remove repeating vertices
    vs, idx = art.get_unique_rows(vs)

    # Assign indices to the new triangle vertices
    v1 = Nx + idx[0:Nt]
    v2 = Nx + idx[Nt:2*Nt]
    v3 = Nx + idx[2*Nt:3*Nt]

    # Define new triangles
    t1 = add_to_array_vertical([tris[:, 0], v1, v3])
    t2 = add_to_array_vertical([tris[:, 1], v2, v1])
    t3 = add_to_array_vertical([tris[:, 2], v3, v2])
    t4 = add_to_array_vertical([v1, v2, v3])

    # New vertices and triagnles:
    xs = np.concatenate((xs, vs), axis=0)

    x_l2 = []
    for elem in xs:
        x_l2 += [np.sqrt(np.sum(elem*elem))]
    x_l2 = np.array(x_l2)
    # ---reshape for [xs / x_l2]
    x_l2 = np.repeat(x_l2, len(xs[0]), axis=0)
    x_l2 = x_l2.reshape(len(xs), len(xs[0]))
    xs = xs / x_l2
    #
    tris = np.concatenate((t1, t2, t3, t4), axis=0)
    tris = np.array(tris).astype(int)
    return xs, tris


def Test_bisectTri():
    tris = np.genfromtxt('tri_bisect_171123.txt', delimiter='  ')
    xs = np.genfromtxt('x_bisect_171123.txt', delimiter='  ')
    tris = tris.astype(int)  # from float
    tris = tris - 1  # from indexing [1..] to [0..]
    resxs, restris = bisectTri(xs, tris)

    print(resxs)
    print(restris)
    '''
    (Pdb) p len(resxs)
    42
    (Pdb) p resxs[:5]
    array([[ 0.        ,  0.85065081,  0.52573111],
           [ 0.        , -0.85065081,  0.52573111],
           [ 0.        ,  0.85065081, -0.52573111],
           [ 0.        , -0.85065081, -0.52573111],
           [ 0.52573111,  0.        ,  0.85065081]])
    (Pdb) p resxs[-5:]
    array([[ 0.80901699, -0.30901699, -0.5       ],
           [ 0.80901699, -0.30901699,  0.5       ],
           [ 0.80901699,  0.30901699, -0.5       ],
           [ 0.80901699,  0.30901699,  0.5       ],
           [ 1.        ,  0.        ,  0.        ]])
    (Pdb) p len(restris)
    80
    (Pdb) p restris[:5]
    array([[ 9, 16, 20],
           [ 2, 19, 28],
           [10, 38, 34],
           [11, 14, 12],
           [ 7, 13, 15]])
    (Pdb) p restris[-5:]
    array([[26, 29, 21],
           [33, 29, 37],
           [34, 25, 33],
           [39, 41, 37],
           [35, 39, 31]])
    '''
    pass  # for breakpoint in pdb

if __name__ == '__main__':
    Test_bisectTri()
