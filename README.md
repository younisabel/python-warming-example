# warming: A Python Project Example

This is an example python project, showing the basic structure of a
larger project. It contains a minimal set of recommended files,
including unit tests and documentation.

# Fork and clone the repository

First, fork the repository from the [original repository link](git@github.com:ChristianHirsch/python-warming-example).
Then, clone the repository from your personal fork with the following code (change USER with your Github
username).

```
git clone git@github.com:USER/python-warming-example
```

# Install conda environment

If not already done, go to the directory and install the conda environment and activate it:

```
cd python-warming-example
conda env create -f ./conda-env.yml
conda activate nature-warming-env
```

# Build and open documentation

Now you are ready to build and open the documentation. With your
conda command prompt, go to the root directory and execute:

```
mkdocs serve
```

Go to the documentation site [http://127.0.0.1:8000/](http://127.0.0.1:8000),
read the documentation and start implementing the features as specified in the
[issues](http://127.0.0.1:8000/issues) site.

# References

This example is based on [Ivanovich, C.C., Sun, T., Gordon, D.R. *et al.* Future warming from global food consumption.
*Nat. Clim. Chang.* **13**, 297–302 (2023).
https://doi.org/10.1038/s41558-023-01605-8](https://www.nature.com/articles/s41558-023-01605-8)
