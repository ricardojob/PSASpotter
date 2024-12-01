from os import path
from setuptools import setup, find_packages
from codecs import open

NAME = "psaspotter"

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name=NAME,
    version="0.0.6",
    license="MIT",
    author="Ricardo Job",
    url="https://github.com/ricardojob/psaspotter",
    description="A tool for extracting of Platform-Specific APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Education :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="platform-specific api detect tool",
    packages=find_packages(include=[NAME]),
    python_requires="~= 3.8",
    install_requires=[
        "click ~= 8.1.7",
        "jsonschema ~= 4.21.0",
    ],
    zip_safe=True,
    # entry_points={"console_scripts": [f"{NAME}={NAME}.main:main"]},
    entry_points={"console_scripts": [f"{NAME}={NAME}.main:main", f"dosa={NAME}.batch:batch"]},
)

# [project.urls]
# "Homepage" = "https://github.com/ricardojob/psae"
# "Bug Tracker" = "https://github.com/ricardojob/psae/issues"

# python3 -m venv psaenv
# source psaenv/bin/activate
# pip3 install -r requirements.txt

## build app
# pip3 install -e .
# python3 -m pip install --upgrade build
# python3 -m build
# python3 -m pip install --upgrade twine

# create a token in respository (PyPi or test.PyPi)
# python3 -m twine upload --repository testpypi dist/*


# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps psaspotter-ricardojob