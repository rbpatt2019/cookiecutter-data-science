# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Getting Started

After installing, be sure to initialise a git hub repo, because VCS is import for reproducibility!

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

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
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
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://github.com/rbpatt2019/cookiecutter-data-science">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
