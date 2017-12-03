import numpy as np
import sys

'''
v0.1 Dec. 03, 2017
  - add getHammersleyNodes()
  - add vdcorput()
  - add get_fliplr()
  - add basexpflip()
  - add Test_getHammersleyNodes()
  - add round_zero_direction()
'''

# %GETHAMMERSLEYNODES Comutes a Hammersley set of nodes on the unit sphere,
# %   which are low-discrepancy sequences of nodes.
# %
# %   X = getHammersleyNodes(N) returns an N-by-3 matrix of Hammersley nodes
# %   on the sphere, which form a low-discrepancy sequence for the sphere.
# %   The columns of X corresponds to the (x,y,z) cordinates of the nodes.
# %
# %   For more details on these node sets see
# %   J. Cui and W. Freeden. Equidistribution on the sphere. SIAM Journal on
# %   Scientific Computing, 18(2):595?609.
# %
# %   Tien-Tsin Wong and Wai-Shing Luk and Pheng-Ann Heng, 1997, Journal of
# %   Graphics Tools , vol. 2, no. 2, 1997, pp 9-24.
# %
# %   Example:
# %       x = getHammersleyNodes(2000);
# %       plotSphNodes(x);
#
# % Author: Grady Wright, 2014
#
#
# % This code uses vdcorput, which was created by Dimitri Shvorob.

# ported by Yasuhiko OKADA (Dec. 3, 2017)


def getHammersleyNodes(nval):
    ts = vdcorput(nval, base=2)
    #
    ts = 2 * ts - 1

    # get odd values such as [1,3,5,...]
    pos = np.arange(1, 2 * nval + 1, 2)
    #
    phi = 2 * np.pi * (pos / 2.0 / nval)
    phi = np.transpose(phi)

    res = []
    for idx, elem in enumerate(ts):
        if idx >= len(ts) - 1:
            break
        wrk = 1.0 - np.power(elem, 2)
        x1 = np.sqrt(wrk) * np.cos(phi[idx])
        x2 = np.sqrt(wrk) * np.sin(phi[idx])
        res += [[*x1, *x2, *elem]]
    return np.array(res)


def vdcorput(kval, base):
    # % VDCORPUT   Base-b Van der Corput sequence, elements 0,..,k
    # % INPUTS   : k - maximum sequence index, non-negative integer
    # %            b - sequence base, integer exceeding 1
    # % OUTPUTS  : s - (k+1)*1 array, with s(i) storing element (i+1)
    # %                of base-b Van der Corput sequence
    # % AUTHOR   : Dimitri Shvorob
    #
    # ported by Yasuhiko OKADA (Dec. 3, 2017)

    if kval != np.floor(kval) or kval < 0:
        print("ERROR:vdcorput() invalid [kval]:", kval)
        sys.exit()
    if base != np.floor(base) or base < 2:
        print("ERROR:vdcorput() invalid [base]:", base)
        sys.exit()

    ss = np.zeros((kval+1, 1))
    for idx in range(kval):
        awrk = basexpflip(idx+1, base)
        ncol = len(awrk[0])
        gs = base ** np.array(range(1, ncol+1))
        ss[idx+1][0] = np.sum(awrk / gs)
    return ss


def basexpflip(kval, base):
    # reversed base-b expansion of positive integer k
    wrk = np.log(kval) / np.log(base)
    jval = round_zero_direction(wrk) + 1.0
    jval = jval.astype(int)[0]

    res = np.zeros((1, jval))

    qval = base**(jval - 1)
    for idx in range(jval):
        res[0][idx] = np.floor(kval / qval)
        kval = kval - qval * res[0][idx]
        qval = qval / base
    return get_fliplr(res)


def get_fliplr(xs):
    xs = np.array(xs)
    if xs.ndim == 1:
        return np.flipud(xs)
    return np.fliplr(xs)


def round_zero_direction(xs):
    xs = np.array(xs)

    # to avoid "TypeError: iteration over a 0-d array"
    # for the array with 1 element
    if xs.ndim == 0:
        xs = [xs]

    #
    res = []
    for elem in xs:
        if elem >= 0.0:
            res += [np.floor(elem)]
        else:
            res += [np.ceil(elem)]
    return np.array(res)


def Test_getHammersleyNodes():
    res = getHammersleyNodes(2025)
    print(res)


if __name__ == '__main__':
    Test_getHammersleyNodes()
