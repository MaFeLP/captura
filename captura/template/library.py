import logging
import shutil
import sys
from os import PathLike
from pathlib import Path
from typing import IO
from zipfile import ZipFile

from yaml import safe_load

from captura.config import config_from_yaml

logger = logging.getLogger(__name__)

template_directory = Path.home() / ".captura" / "templates"

# Change on linux to use the XDG Base Directory Specification
if sys.platform == "linux" or sys.platform == "linux2":
    from xdg.BaseDirectory import xdg_data_dirs

    template_directory = Path(xdg_data_dirs[0]) / "captura" / "templates"

if not template_directory.exists():
    template_directory.mkdir(parents=True)


def load_new_template(file_path: str | PathLike[str] | IO[bytes]):
    """Load a new template to the library

    :param file_path: The file path to the ZIP compressed template file

    :raises KeyError: When a key is missing in the config.yaml file of the template
    :raises ValueError: When a key has the wrong type in the config.yaml file of the template
    :raises YAMLError: When the config.yaml file of the template is not parseable
    """
    archive = ZipFile(file_path, "r")
    config = config_from_yaml(safe_load(archive.read("config.yml")))
    logger.debug(f"Loaded valid configuration for template '{config.id}' version '{config.version}'")

    new_template_directory = template_directory / f"{config.id}-{config.version}"

    # Check if template already exists and replace if necessary
    if new_template_directory.exists():
        logger.info(f"Template '{config.name}' version '{config.version}' already exists")
        shutil.rmtree(new_template_directory)
        logger.info("Old directory has been removed")

    new_template_directory.mkdir(parents=True)
    archive.extractall(new_template_directory)
    logger.debug(f"Extracted template to '{new_template_directory}'")

    logger.info(f"Loaded template '{config.id}' version '{config.version}'")
