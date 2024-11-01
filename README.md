[![Tests](https://github.com/ricardojob/PSASpotter/actions/workflows/tests.yaml/badge.svg)](https://github.com/ricardojob/PSASpotter/actions/workflows/tests.yaml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/psaspotter)](https://pypi.org/project/psaspotter/)

<!-- ![Maven](https://github.com/VariantSync/SyncStudy/actions/workflows/maven.yml/badge.svg) -->
<!-- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7025599.svg)](https://doi.org/10.5281/zenodo.7025599)
[![Documentation](https://img.shields.io/badge/Documentation-read%20here-blue)][documentation]
[![Requirements](https://img.shields.io/badge/System%20Requirements-read%20here-blue)](INSTALL.md)
[![Install](https://img.shields.io/badge/Installation%20Instructions-read%20here-blue)](INSTALL.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE) -->

# PSASpotter

An automated tool for extracting Platform-Specific API from Git repositories written in Python. 
The `psaspotter` (**P**latform-**S**pecific **A**PI Spotter) is primarily designed to be used as a command-line tool. 
With `psaspotter`, you can easily extract information about the Platform-Specific APIs and their usages from the Git repository or directory (only python files are analyzed).
The set of Platform-Specific APIs are saved in a given CSV file.

## Install

The easiest way to install `psaspotter` is to install from Pypi

```
pip install psaspotter
```

Alternatively, you can install from `test environment`
```
pip install --index-url https://test.pypi.org/simple/ --no-deps psaspotter
```

You may wish to use this tool in a virtual environment. You can use the following commands.

```
virtualenv psaspotter_venv
source psaspotter_venv/bin/activate
pip install psaspotter
```

## Quick examples

As an example, the following command extracts every platform-specific APIs from the directory `repository_local`. 
It also saves various information (line, module, filename ...) in `output.csv`. 
Additionally, we can provide information about the project present in the directory provided. 
For this, the parameters `-n` and `-c` can be added to inform the name (`my/local`) and last commit (`da39a3ee5e6b4b0d3255bfef95601890afd80709`) of the project. 
This information will be available in the output file.

```bash
psaspotter repository_local -o output.csv -n my/local --commit da39a3ee5e6b4b0d3255bfef95601890afd80709 
```

Note that the repository does not have to be already cloned, the tool also can fetch it. 
For example, the GitHub repository `https://github.com/ricardojob/PSASpotter` will be fetched, saved under the `data/PSASpotter` directory.
Note that, by default all projects are cloned to the `data` directory.

```bash
psaspotter https://github.com/ricardojob/PSASpotter -o output.csv
```

## Usage

After installation, the `psaspotter` command-line tool should be available in your shell. 
Otherwise, please replace `psaspotter` by `python -m psaspotter`. 
The explanations in the following stays valid in both cases.

You can use `psaspotter` with the following arguments:

```
Usage: psaspotter [OPTIONS] REPOSITORY

  Extract the usage of Platform-Specific APIs from a single Git repository
  `REPOSITORY`. The Git repository can be local or remote. In the latter case,
  it will be pulled locally in the folder `data`. Every extracted Platform-
  Specific APIs will be written in the CSV file given to `-o`, or in the
  standard output if not specified.

  Example of usage: psaspotter myRepository -n myRepositoryName -o output.csv

Options:
  -o, --output FILE           The output CSV file where the usage of Platform-
                              Specific APIs related to the repository will be
                              stored. By default, the information will written
                              to the standard output.
  -c, --commit TEXT           The commit reference (i.e., commit SHA or TAG)
                              to be considered for the extraction.It is
                              important to note that each commit references a
                              local project.
  -n, --repository-name TEXT  The name's project to be considered for the
                              extraction.It is important to note that the name
                              references a local project.
  -p, --platforms [all|OS]    The Platform-specific API group to figure out.
  -f, --filter FILE           The JSON file with the configuration of
                              Platform-Specific APIs that will be filter. By
                              default, this option is mandatory to option
                              --platforms.
  -h, --help                  Show this message and exit.
```

The CSV file given to `-o` (or that will be written to the standard output by default) will contain the following columns:
- `project_name`: the name of the repository
- `project_commit`: the commit SHA of the commit where the platform-specific APIs file was extracted
- `line`: the line where the platform-specific API usage occurs
- `module`: the module that packages the platform-specific API
- `call`: a short information about of platform-specific API
- `is_test`: a boolean indicating if the file is a test file
- `url`: the URL that represents the API usage on Github
- `risk`: the (low or right) risk for this instance

## License

Distributed under [MIT License](https://github.com/ricardojob/PSASpotter/blob/main/LICENSE.txt).

## Acknowledgements

The structure of this project was heavily inspired by the [gigawork](https://github.com/cardoeng/gigawork) and [spotflow](https://github.com/andrehora/spotflow) projects.