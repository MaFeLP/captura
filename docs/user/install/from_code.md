---
title: Install from Code
parent: Installation
layout: default
---

# Installation from Source Code
## Install Prerequisities
Install [Poetry](https://python-poetry.org/docs/#installation) for dependency management.

## Get the source code
Navigate to the [Project's homepage](https://github.com/MaFeLP/captura/) and download the source code.

![The GitHub Project page with markers on where to click]({% link user/install/dl_github_source_code.png %})

Unzip the ZIP-Archive and navigate in a terminal to this directory. On windows, this can be done by using the
File explorer to navigate to the extracted folder, clicking on the address bar and typing `powershell`. Afterwards,
enter the following commands:

```bash
poetry install
poetry run python3 -m captura
```

