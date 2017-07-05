# Dask Tutorial for PyData Seattle 2017

This contains materials for the dask tutorial [Parallelizing Scientific Python
with Dask](https://pydata.org/seattle2017/schedule/presentation/58/).

## Setup

This tutorial is designed to run in an online environment. You shouldn't need
to install anything, instead just go to the following link and click the big
blue button:

[https://pycon-parallel.jovyan.org](https://pycon-parallel.jovyan.org)

### Running Locally

If you want to run this tutorial locally instead, you can use the following
instructions. Note that the material in notebooks 3 & 4 will not work 100%
without the environment setup in the link above. Everything else should work
fine though.

To setup locally, clone the repo and install all required dependencies:

```bash
$ git clone https://github.com/jcrist/dask-tutorial-pydata-seattle-2017
$ conda install dask distributed matplotlib s3fs jupyter -c conda-forge
$ pip install graphviz
```

Then start a jupyter notebook inside the cloned directory

```bash
$ cd dask-tutorial-pydata-seattle-2017
$ jupyter notebook
```

## Acknowledgements

This tutorial wouldn't be possible without the work done by the larger Dask
community implementing much of the functionality found here. The materials here
are based off of a [previous dask
tutorial](https://github.com/mrocklin/dask-workshop) by Matt Rocklin.

We also thank Google for generously providing compute credits on [Google
Compute Engine](https://cloud.google.com/compute/), which was backed the
distributd clusters used during the tutorial at PyData Seattle.
