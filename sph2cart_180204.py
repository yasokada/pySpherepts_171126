import numpy as np

'''
v0.3 Feb.04, 2018
    - can be used by "import"
    - renamed to [sph2cart_180204]
v0.2 Feb.04, 2018
    - convert all elements at one
        + sph2cart() processes a set
v0.1 Feb.04, 2018
    - convert each element
        + add sph2cart()
'''

# testd on Python 3.5.2
# coding rule:PEP8


def sph2cart(azimuth, elevation, radius):
    axs = np.cos(azimuth) * np.sin(np.pi/2 - elevation) * radius
    ays = np.sin(azimuth) * np.sin(np.pi/2 - elevation) * radius
    azs = np.cos(np.pi/2 - elevation) * radius
    return axs, ays, azs


def test_cubic_8vertices():
    AZS = [0.7854, 0.7854, -0.7854, -0.7854, 2.3562, 2.3562, -2.3562, -2.3562]
    ELS = [0.6155, -0.6155, 0.6155, -0.6155, 0.6155, -0.6155, 0.6155, -0.6155]
    RS = [1.7321] * len(AZS)

    azs = np.array(AZS)
    els = np.array(ELS)
    rs = np.array(RS)

    axs, ays, azs = sph2cart(azs, els, rs)
    np.set_printoptions(precision=5)  # for debug
    print(axs)
    print(ays)
    print(azs)


if __name__ == '__main__':
    test_cubic_8vertices()
