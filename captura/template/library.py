import logging
import shutil
from os import PathLike
from typing import IO
from zipfile import ZipFile

from yaml import safe_load, YAMLError

from captura.config import config_from_yaml, Config
from captura.environment import template_directory

logger = logging.getLogger(__name__)


def load_new_template(file_path: str | PathLike[str] | IO[bytes]):
    """Load a new template to the library

    :param file_path: The file path to the ZIP compressed template file

    :raises KeyError: When a key is missing in the config.yaml file of the template
    :raises ValueError: When a key has the wrong type in the config.yaml file of the template
    :raises YAMLError: When the config.yaml file of the template is not parseable
    """
    archive = ZipFile(file_path, "r")
    config = config_from_yaml(safe_load(archive.read("config.yml")))
    logger.debug(
        f"Loaded valid configuration for template '{config.id}' version '{config.version}'"
    )

    new_template_directory = template_directory / f"{config.id}-{config.version}"

    # Check if template already exists and replace if necessary
    if new_template_directory.exists():
        logger.info(
            f"Template '{config.name}' version '{config.version}' already exists"
        )
        shutil.rmtree(new_template_directory)
        logger.info("Old directory has been removed")

    new_template_directory.mkdir(parents=True)
    archive.extractall(new_template_directory)
    logger.debug(f"Extracted template to '{new_template_directory}'")

    logger.info(f"Loaded template '{config.id}' version '{config.version}'")


def get_library_templates() -> list[Config]:
    """Get a list of all templates in the library

    :return: A list of tuples with the template id and name
    """
    out = []
    logger.debug("Getting templates from library")
    for template in template_directory.iterdir():
        logger.debug(f"Checking template '{template}'")
        if template.is_dir():
            if not (template / "config.yml").exists():
                logger.error(f"Template '{template}' has no configuration, skipping...")
                continue
            try:
                logger.debug(f"Reading configuration for template '{template}'")
                with open(template / "config.yml", "r") as file:
                    out.append(config_from_yaml(safe_load(file.read())))
            except (KeyError, ValueError, TypeError, YAMLError) as e:
                logger.error(
                    f"Template '{template}' has an invalid configuration, skipping..."
                )
                logger.error(e)
                continue
    return out
