# Dask Tutorial for PyData Seattle 2017

This contains materials for the dask tutorial [Parallelizing Scientific Python
with Dask](https://pydata.org/seattle2017/schedule/presentation/58/).

## Installation

To setup, clone the repo and install all required dependencies:

```bash
$ git clone https://github.com/jcrist/dask-tutorial-pydata-seattle-2017
$ conda install dask distributed jupyter -c conda-forge
$ pip install graphviz
```

## Acknowledgements

This tutorial wouldn't be possible without the work done by the larger Dask
community implementing much of the functionality found here. The materials here
are based off of a [previous dask
tutorial](https://github.com/mrocklin/dask-workshop) by Matt Rocklin.

We also thank Google for generously providing compute credits on [Google
Compute Engine](https://cloud.google.com/compute/), which was backed the
distributd clusters used during the tutorial at PyData Seattle.
