install:
	pip3 install -U poetry
	poetry install

optional:
	poetry run pip install black mypy

style:
	poetry run isort -rc --atomic .
	poetry run black .
	poetry run flake8

type:
	poetry run mypy --ignore-missing-imports tests doccron

check:
	poetry run safety check
	poetry run bandit -r doccron

test:
	poetry run pytest --cov=doccron --cov-report=xml --cov-report=html -vv