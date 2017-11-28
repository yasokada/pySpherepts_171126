import numpy as np


'''
v0.1 Nov. 25, 2017
  - add get_unique_rows()
'''


def get_unique_rows(vs):
    unqs = np.unique(vs, axis=0)
    idxs = []
    for alist in vs:
        wrk, _ = np.where(unqs == alist)
        loc = -1
        for idx in wrk:
            if (unqs[idx] == alist).all():
                loc = idx
                break
        idxs += [loc]
    return np.array(unqs), np.array(idxs)
