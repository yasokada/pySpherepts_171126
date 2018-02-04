import numpy as np
import sph2cart_180204 as s2c

# %% GETFIBONACCINODES 
# % Computes Fibonacci (or phyllotaxis) node sets for the surface of the sphere.
# %
# % X = getFibonacciNodes(N) returns an N-by-3 matrix containing the 
# %   Fibonacci nodes, where N must be odd. The columns corresponds
# %   to the (x,y,z) cordinates of the nodes.  Note that these nodes are only
# %   unique up to a roataion.
# %
# % There are different ways to generate the Fibonacci nodes. This code uses the 
# % method advocated by Swinbank and Pruser:
# %
# % R. Swinbank and R. James Purser, Fibonacci grids: A novel approach to
# % global modelling, Quarterly Journal of the Royal Meteorological Society,
# % 132 (2006), pp. 1769-1793.
# % 
# % This construction avoids placing any nodes at the poles.
# 
# % Author: Grady Wright, 2014

# ported by Yasuhiko OKADA


'''
v0.2 Feb.04, 2018
    - refactor
v0.1 Feb.04, 2018
    - add getFibonacciNodes()
'''

# tested on Python 3.5.2
# tested on sph2cart_180204 v0.3
# coding rule:PEP8


def getFibonacciNodes(Num):
    Nhalf = np.ceil(Num // 2).astype(np.int)
    Nodd = 2 * Nhalf + 1
    lat, lon = [0.0] * Nodd, [0.0] * Nodd
    golrat = (1 + np.sqrt(5))/2  # golden ratio

    xs = []
    for pickidx in range(-Nhalf, Nhalf + 1):
        lat = np.arcsin(2*pickidx/Nodd)
        lon = 2 * np.pi * pickidx / golrat
        res = s2c.sph2cart(lon, lat, 1+0.0*lat)
        xs += [res]
    xs = np.array(xs)
    return xs


def Test_even_odd():
    res = getFibonacciNodes(3)
    print(res)
    res = getFibonacciNodes(4)
    print(res)


if __name__ == '__main__':
    Test_even_odd()
