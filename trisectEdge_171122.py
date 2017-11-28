import numpy as np

'''
v0.2 Nov. 23, 2017
  - add Test_trisectEdge()
v0.1 Nov. 22. 2017
  - add trisectEdge()
'''


def trisectEdge(x1, x2):
    dp = np.sum(x1 * np.transpose(x2))
    alp = 1/3 * np.arccos(dp)
    denom = dp*dp - 1
    #print(np.cos(alp))
    c1 = (dp * np.cos(2 * alp) - np.cos(alp)) / denom
    c2 = (dp * np.cos(alp) - np.cos(2*alp)) / denom
    x = [x1*c1 + x2*c2, x2*c1 + x1*c2]
    return np.array(x)


def Test_trisectEdge():
    ans = np.array([
        [-0.8520, 0.3955, 0.3431],
        [-0.7386, 0.2120, 0.6399],
        ])
    x1 = np.array([-0.8507, 0.5257, 0.0])
    x2 = np.array([-0.5257, 0.0, 0.8507])
    wrk = trisectEdge(x1, x2)
    print(wrk)
    print(ans)


if __name__ == '__main__':
    Test_trisectEdge()
