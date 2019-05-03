# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

Customised to a few of my preferences, including:

1. Using setup.cfg over tox.ini
1. Incorporating pytest into setup.py
1. Requiring pytest-mypy and pytest-instafail for tests
1. Move tests into a directory
1. Using GPL3 as a license
1. Adding black and isort to `make lint`
1. Adding `make test` command
1. Clearing default code in `make_dataset.py`

#### [Original CookieCutter](http://drivendata.github.io/cookiecutter-data-science/)
#### [Project Repo](https://github.com/rbpatt2019/cookiecutter-data-science)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or >3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### Getting started:
------------

To begin a new project, call cookiecutter with the template name:

```bash
$ cookiecutter gh:rbpatt2019/cookiecutter-data-science
```

After creating your project, be sure to initialise a git hub repo, because VCS is import for reproducibility!

```bash
cd {{cookiecutter.project_name}}
git init
git add .
git commit
git tag -a 0.1.0
```

Then, create a new virtual environment for the project! If you use conda or virtualenv with virtualenvwrapper, you can run:

```bash
make create_environment
```

Otherwise, create a virtual environment according to your workflow. Once created, be sure to install the requirements. Run:

```bash
make requirements 
```

Now you are good to go! Run `make clean` to remove compiled files and `make lint` to int your files with black, isort, and flake8. Tests should be put in the tests directory and can be run with `make test` which lints your files then runs pytest with mypy and instafail.

If you run `make data`, the script `make_dataset.py` will be run in the current environment. This is useful for reading your raw data into pandas, eg. 



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── tests              <- Folder for py.test test files
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── setup.cfg          <- Configuration for setup.py
```

## Contributing

I welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

