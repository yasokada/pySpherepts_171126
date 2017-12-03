
# coding: utf-8

# In[32]:

'''
HammersleyNodes 
'''

import numpy as np
from pylab import rcParams
import getHammersleyNodes_171203 as gHN
import plotSphNodes_171127 as pSN

rcParams['figure.figsize'] = 10,10
rcParams['figure.dpi'] = 75

xs = gHN.getHammersleyNodes(100)

elev, azm = 30.0, -30.0

#NG: hidden by the central sphere
pSN.plotSphNodes(xs, elevation=elev, azimuth=azm)

# *1.05: required not to be hidden by the central sphere
pSN.plotSphNodes(xs * 1.05, elevation=elev, azimuth=azm)

print(xs)


# In[ ]:



