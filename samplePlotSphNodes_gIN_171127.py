
# coding: utf-8

# In[1]:

'''
Type 0 Example
(See. [NodesGridsMeshesOnSphere.pdf] of [spherepts] by Prof. Grady Wright)
view(90,0) in MATLAB
'''
import numpy as np
from pylab import rcParams
import getIcosNodes_171126 as gIN
import plotSphNodes_171127 as pSN

rcParams['figure.figsize'] = 10,10
rcParams['figure.dpi'] = 75

xs, tris = gIN.getIcosNodes(4,0)
pSN.plotSphNodes(xs, elevation=0.0, azimuth=90.0)

print(xs)
print(tris)


# In[2]:

'''
Type 1 Example
(See. [NodesGridsMeshesOnSphere.pdf] of [spherepts] by Prof. Grady Wright)
view(90,0) in MATLAB
'''
import numpy as np
from pylab import rcParams
import getIcosNodes_171126 as gIN
import plotSphNodes_171127 as pSN

rcParams['figure.figsize'] = 10,10
rcParams['figure.dpi'] = 75

xs, tris = gIN.getIcosNodes(2,1)
pSN.plotSphNodes(xs, elevation=0.0, azimuth=90.0)

print(xs)
print(tris)


# In[ ]:



