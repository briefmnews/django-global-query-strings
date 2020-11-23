install:
	pip install -r requirements_tests.txt

release:
	- python setup.py sdist bdist_wheel
	- python -m twine upload --repository testpypi dist/*
