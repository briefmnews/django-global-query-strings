install:
	pip install -r requirements_tests.txt

release_test:
	- rm -rf build && rm -rf dist && rm -rf *.egg-info
	- python setup.py sdist bdist_wheel
	- python -m twine upload --repository testpypi dist/*

release_prod:
	- rm -rf build && rm -rf dist && rm -rf *.egg-info
	- python setup.py sdist bdist_wheel
	- python -m twine upload dist/*
