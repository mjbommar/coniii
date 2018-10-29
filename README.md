[![PyPI version fury.io](https://badge.fury.io/py/coniii.svg)](https://pypi.python.org/pypi/coniii/) [![PyPI license](https://img.shields.io/pypi/l/coniii.svg)](https://pypi.python.org/pypi/coniii/)

# Convenient Interface to Inverse Ising

ConIII is a Python package for solving maximum entropy problems with a focus on the pairwise maximum
entropy model, also known as the inverse Ising problem. Support for Python 3.6 only (v0.2.10 works
with Python 2.7 but is no longer actively maintained).

If you use ConIII for your research, please cite the following:
> Lee, Edward D. and Daniels, Bryan C.  Convenient Interface to Inverse Ising (ConIII): A Python package for solving maximum entropy models.  arXiv preprint:1801.08216 (2018).

The link to the arXiv article is here: [https://arxiv.org/abs/1801.08216]. 

Documentation is included in the docs/\_build/html/index.html webpage. Unfortunately, the online
documentation on readthedocs.org seems to compiling properly but the functions are not displaying!

## Installation
This package is available on PyPI. It can be installed by running  
```bash
$ pip install coniii
```

If you have trouble using `pip` and PyPI, then you can always build this package from source.
Download the latest release from GitHub and move the "coniii" folder to wherever you would like to have
the module (make sure this folder is in your file path and that you are running Python 3.6).  Inside
"coniii", you must run
```bash
$ pip install .
```

Note: Using setuptools in the usual way of `python setup.py install` will not work because eggs are
incompatible with cached jit functions.

If you would like to use the `Enumerate` solver for system sizes greater than 9, you must run
enumerate.py to write those files yourself. This can be run from the install directory.  If you do
not know where the installation directory is, you can find it by starting a Python terminal and
running
```bash
$ import coniii
$ coniii.__path__
```

Once inside the install directory, you can run in your bash shell
```bash
$ python enumerate.py [N]
```

where `[N]` should be replaced by the size of the system. For more details, see the \_\_main\_\_ block
at the end of the file enumerate.py.

## Quick guide

A Jupyter notebook with examples for how to use ConIII is available in the ipynb directory on
the Github repository: [https://github.com/eltrompetero/coniii/blob/master/ipynb/usage_guide.ipynb].
There is a brief introduction as well in there.

The notebook is installed into your coniii package directory if you used pip, or you can download it
from the above Github link.

First copy the notebook file `usage_guide.ipynb` into a directory outside the ConIII directory.
Change to this directory and run
```bash
$ jupyter notebook
```

This should open the notebook in your default web browser.

## Dependencies

In order to run the usage guide Jupyter notebook, you must have both Jupyter and matplotlib
installed. These are automatically installed into your Python path when you install ConIII through
listed dependencies. If you prefer to install them yourself, you can use the Python package
[pip](https://pypi.org/project/pip/). Open a terminal and run
```bash
$ pip install jupyter matplotlib
```

However, we strongly recommend that you use the [Anaconda](https://www.anaconda.com/download/)
package manager, in which case you can install the packages by running
```bash
$ conda install jupyter matplotlib
```

## Troubleshooting
This package is only maintained for Python 3.6 as of October 2018. Make sure that you are running
Python 3.6 which you can check by running in your bash terminal
```bash
$ python --version
```

ConIII has been tested on the following systems
* Debian 9 (Stretch)
* Mac OS X 10.13 (High Sierra)

Some users may encounter difficulties with the multiprocess module, in which case the `n_cpus` kwarg
can be set to 0 when the algorithm class instance is declared.  This will disable the parallel computing functionality provided by the multiprocess module.

### Support
Please file an issue on the GitHub if you have any problems or feature requests.
