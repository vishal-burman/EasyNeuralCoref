install:
	pip install -e . --no-cache-dir

test-install:
	python -m unittest

clean:
	rm -rf **/__pycache__ **/**/__pycache__

check: test-install clean
