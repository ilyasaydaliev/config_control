PY ?= python3

.PHONY: run test lint
run:
	$(PY) src/main.py $(ARGS)

test:
	PYTHONPATH=src $(PY) -m unittest discover -s tests -v

lint:
	$(PY) -m flake8 --max-line-length 80 src tests
