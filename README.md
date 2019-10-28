# Cookiecutter Data Science

A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.

#### [Original CookieCutter](http://drivendata.github.io/cookiecutter-data-science/)

#### [Project Repo](https://github.com/rbpatt2019/cookiecutter-data-science)

You need  installed to complete the setup of this cookiecutter!

## Requirements to use the cookiecutter template:

- Python >3.5
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0.
- [poetry](https://eustace.poetry.io)

## Using the template

When starting a new project, always create a new virtual environment. I use pyenv for all my env/venv control, so I would do:

```sh
pyenv virtualenv project_name
pyenv virtualenv activate project_name
pip install -U cookiecutter
```

Use whatever method is already part of your workflow. Now, we initialise the project:

```sh
cookiecutter https://github.com/rbpatt2019/cookiecutter-pip-click
```

You'll be walked through some prompts to provide the necessary information. And, viola! Your project is set-up! 

## Final Steps

Let's take a peek around. To do that, move into the directory and view it's contents.

```sh
cd project_name
ls
```

Poetry uses a pyproject.toml for all of its settings, so let's look at that.

```sh
cat pyproject.toml
```

Here is where you can modify any settings for the package that you'd like to. The eagle-eyed among you might have noticed that pytest does not have its own section. Currently, pytest does not parse pyproject.toml for settings, so all options are manually passed to pytest in the Makefile.

I think `make` is the greatest thing since sliced bread, so let's check that out.

```sh
cat Makefile
```

Some useful commands here to handle everything from linting to version control to packaging. Since we are going to be developing this tool, run:

```sh
make develop
```

*DO THIS BEFORE ANYTHING ELSE*. I considered adding it to the post-generation hook, but elected not to. This was, you can create a venv however you want to, and I won't bork your python install if you forget to before creating a new project.

Now, create a repo on git hub, and push your new project there.

```sh
git remote add origin https://github.com/YOUR_USER/project_name
git push origin master
```

Happy coding!

## The resulting directory structure

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
└── pyporiject.toml    <- Configuration for setup.py
```

## Contributing

I welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

