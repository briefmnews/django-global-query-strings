from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-global-query-strings",
    version="0.4.0",
    description="Django global query strings allows adding query strings (query params) site-wide",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/briefmnews/django-global-query-strings",
    author="Brief.me",
    author_email="tech@brief.me",
    license="MIT",
    packages=["global_query_strings"],
    python_requires=">=3.7",
    install_requires=[
        "beautifulsoup4>=4",
        "Django>=3",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    zip_safe=False,
)
