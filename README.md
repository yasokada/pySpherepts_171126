Updated: Dec. 03, 2017

### pySpherepts_171126

The Numpy+Scipy version of the "spherepts" ported by Yasuhiko OKADA.

Original MATLAB code by Prof. Grady Wright:
https://github.com/gradywright/spherepts

## Requirements

### Numpy and Scipy 

The code uses Numpy and Scipy.

For Ubuntu 16.04 LTS, the setup procedure is written in the 'doc/setupUbuntu1604LTS.md`.

### freeBoundary

The code uses the [freeBoundary_171112.py].
https://github.com/yasokada/numpy_freeBoundary_171112

Download the above script and put it in the same directory as the [getIcosNodes_171126.py].

## Example

### In Numpy + Scipy Environment

```bash
$ python3 getIcosNodes_171126.py 
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
```

### In Jupyter Notebook (with Numpy and Scipy)

For getIcosNodes()
1. Open the samplePlotSphNodes_gIN_171127.ipynb
2. Execute the Type 0 Example
    - Ctrl + Enter (at Ubuntu 16.04 LTS, for example)
3. Execute the Type 1 Example

For getHammersleyNodes()
1. Open the samplePlotSphNodes_gHN_171203.ipynb
2. Execute the example
    - Ctrl + Enter (at Ubuntu 16.04 LTS, for example)
    
### Porting History

- Dec. 03, 2017: getHammersleyNodes() has been ported
- Nov. 29, 2017: getIcosNodes() has been ported

### Tested environment

```
Ubuntu 16.04 LTS desktop amd64
Python 3.5.2
Numpy v1.13.1
scipy v0.19.1
IPython 6.0.0 -- An enhanced Interactive Python.
```

