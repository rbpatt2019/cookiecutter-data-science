clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/

develop:
	poetry install

install: 
	poetry install --no-dev

format: clean
	isort -rc src
	black src

lint: format
	pyflakes src
	poetry check

test: lint
	poetry run pytest --ignore=docs --verbose --instafail --mypy --mypy-ignore-missing-imports --doctest-modules --cov=src/ --cov-report term

data: clean
	python3 src/data/make_dataset.py

features: data
	python3 src/features/build_features.py

train: features
	python3 src/models/train_model.py

predict: train
	python3 src/models/predict_model.py

visualize: predict
	python3 src/visualization/visualize.py

patch: test
	poetry version patch
	git push origin master --tags

minor: test
	poetry version minor
	git push origin master --tags

major: test
	poetry version major
	git push origin master --tags

dist: clean 
	poetry build

release: dist
	poetry publish

.PHONY: clean develop install format lint test data features train predict visualize patch minor major dist release
