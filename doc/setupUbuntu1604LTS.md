Ubuntu 16.04 LTS > setup Jupyter (Python3 + Numpy + Scipy + Matplotlib)
Updated: Dec. 2, 2017

```txt:environment
Ubuntu 16.04 LTS desktop amd64
```

### Setup Jupyter (Python3 + Numpy + Scipy)

Following is the procedure to setup [Jupyter notebook](http://jupyter.org/) together with [Python3 pip](https://pypi.python.org/pypi), [Numpy](http://www.numpy.org/), and [Scipy](https://www.scipy.org/) .

```bash
$sudo apt-get update
$sudo apt-get install python3-pip
$sudo pip3 install jupyter
> You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
$sudo pip3 install scipy
```

### Setup Matplotlib

[The Matplotlib](https://matplotlib.org/) is used to display processed data in a varierty of graphs.

```bash
$sudo pip3 install matplotlib
```

### Setup Git

```bash
$sudo apt-get install git
```

### Optional (update of pip)

During the [Setup Jupyter], following messages are shown.

> You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

For Python3 pip, following command is used to upgrade the pip version.

```bash
$sudo pip3 install --upgrade pip
```

It is noted that **the pip** shown in this environment is the Python2 pip not the Python3 pip. 

### Trouble shooting

During the procedure shown above, following error messages sometimes appear. 

```
E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
E: Unable to lock directory /var/lib/apt/lists/
E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)
E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?
```

In this case, following commands are used to avoid the error.

```bash
$sudo rm /var/lib/apt/lists/lock
$sudo rm /var/lib/dpkg/lock
```
