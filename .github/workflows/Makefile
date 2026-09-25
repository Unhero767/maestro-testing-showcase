.PHONY: test install clean lint

install:
	pip install -r requirements.txt
	pip install -e .

test:
	PYTHONPATH=. pytest -v

lint:
	flake8 src tests

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .coverage htmlcov
	find . -type d -name "__pycache__" -exec rm -r {} +
