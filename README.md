### pySpherepts_171126

The Numpy+Scipy version of the "spherepts" ported by Yasuhiko OKADA.


## Requirments

### Numpy and Scipy 

The code uses Numpy and Scipy.

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

1. Open the samplePlotSphNodes_gIN_171127.ipynb
2. Execute the Type 0 Example
    - Ctrl + Enter (at Ubuntu 16.04 LTS, for example)
3. Execute the Type 1 Example

    
### Porting History

- Nov. 29, 2017: getIcosNodes() has been ported

### Tested environment

```
Ubuntu 16.04 LTS desktop amd64
Python 3.5.2
IPython 6.0.0 -- An enhanced Interactive Python.
scipy v0.19.1
```

