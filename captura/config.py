import logging
from dataclasses import dataclass
from pathlib import Path
from string import ascii_letters, digits
from typing import Type

from captura.environment import template_directory

logger = logging.getLogger(__name__)


def __validate_field(obj: dict, path: list[str], name: str, field_type: Type) -> None:
    """Valides a field in the config

    :param obj: The object to check
    :param path: The path that will be displayed in the error message to make error handling easier
    :param name: The name of the field on the object parameter
    :param field_type: The type of the field to check against

    :raises KeyError: When the field is missing
    :raises ValueError: When the field is of the wrong type
    """
    if not name in obj:
        raise KeyError(f"Missing required field '{'.'.join(path)}.{name}'")
    if not isinstance(obj[name], field_type):
        raise ValueError(
            f"Field '{'.'.join(path)}.{name}' must be a {field_type.__name__}"
        )


def __validate_section(section: dict, section_idx: int) -> None:
    """Valides a section in the config

    :param section: The section to check
    :param section_idx: The list index of the section in the config

    :raises KeyError: When a field is missing from the section
    :raises ValueError: When a field is of the wrong type
    """
    __validate_field(section, ["sections"], "name", str)
    __validate_field(section, ["sections"], "description", str)
    __validate_field(section, ["sections"], "fields", list)

    for idx, field in enumerate(section["fields"]):
        __validate_field(
            field, [f"sections[{section_idx}]", f"fields[{idx}]"], "id", str
        )
        __validate_field(
            field, [f"sections[{section_idx}]", f"fields[{idx}]"], "label", str
        )
        __validate_field(
            field, [f"sections[{section_idx}]", f"fields[{idx}]"], "type", str
        )
        for char in field["id"]:
            if char not in ascii_letters + digits + "_":
                raise ValueError(
                    f"Field 'sections.[{idx}].id' contains invalid characters"
                )
        if not field["type"] in ["text", "checkbox", "select", "list"]:
            raise ValueError(
                f"Field 'sections.[{idx}].type' has incorrect type '{field['type']}'"
            )


def validate(config: dict) -> None:
    """Check the config for correctness

    :param config: The config to check

    :raises KeyError: When a required field is missing
    :raises ValueError: When a field has the wrong type or incorrect characters
    """
    logger.debug("Validating configuration")
    for string in ["name", "description", "id", "version", "author", "license"]:
        __validate_field(config, [], string, str)

    for l in ["files", "tags", "sections"]:
        __validate_field(config, [], l, list)

    for idx, section in enumerate(config["sections"]):
        __validate_section(section, idx)
    logger.info(f"Found valid configuration '{config['id']}-{config['version']}'")


@dataclass
class Field:
    """A specific field of a section"""

    id: str
    """The id of the field, will be the variable name in the template"""

    label: str
    """The label of the field, will be shown in the wizard to the use"""

    type: str
    """The type of the field, can be 'text', 'checkbox' or 'select'"""

    default: str = ""
    """The default value of the field"""

    when: str = ""
    """The condition for the field to be shown"""


@dataclass
class Section:
    """A section of the wizard"""

    name: str
    """The name of the section"""

    description: str
    """The description of the section"""

    fields: list[Field]
    """The fields of the section"""


@dataclass
class Config:
    """The configuration of a template"""

    name: str
    """The name of the template"""

    description: str
    """The description of the template"""

    id: str
    """The id of the template in reverse domain notation"""

    version: str
    """The version of the template without the 'v'"""

    author: str
    """The author of the template"""

    license: str
    """The license of the template"""

    tags: list[str]
    """The tags of the template"""

    files: list[str] | str
    """The files that the template should apply to"""

    sections: list[Section]
    """Sections for the wizard of the template"""

    single_file: bool = False
    """Whether the template is a single file template or a multi file template"""

    assets: list[str] | None = None
    """Assets of the template that will just be copied into the output directory. Needs 'single_file' to be False"""

    def get_directory(self) -> Path:
        """Get the directory where the template is stored

        :return: The directory
        """
        return template_directory / f"{self.id}-{self.version}"


def config_from_yaml(yaml: dict) -> Config:
    """Create a config struct from a yaml dict

    :param yaml:
    :return: The config object
    """
    validate(yaml)
    return Config(**yaml)
