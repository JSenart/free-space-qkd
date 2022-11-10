init:
	python -m pip install -r requirements.txt

test:
	py.test tests

run:
	python qkd/main.py

.PHONY: init test