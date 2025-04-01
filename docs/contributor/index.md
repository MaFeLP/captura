---
title: Contributing
layout: default
---

# Contributing
## Reporting an issue
You can report an issue and suggestions at <https://github.com/MaFeLP/captura/issues>. Please make sure, you have searched
for similar issues before. To allow for easy troubleshooting, please include the log output of the program and/or fitting
screenshots.

## Set up the development environment
Install [Poetry](https://python-poetry.org/) for dependency management.

Get the source code and run the development build:

```bash
git clone https://github.com/MaFeLP/captura.git
cd captura
poetry install
```

You can now run the development build using poetry:

```bash
poetry run python3 -m captura
```

## Coding Style
We use the [black](https://black.readthedocs.io/en/stable/index.html) coding style.
Before comming your changes, please format your changes using black:

```bash
poetry run black captura
```

## Filing a Pull Request
Contributions are very welcome! For this, please for the repository and open a [pull request](https://github.com/MaFeLP/captura/pulls)!

