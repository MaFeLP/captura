import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from string import ascii_letters, digits
from typing import Type

logger = logging.getLogger(__name__)


def __validate_field(obj: dict, path: list[str], name: str, field_type: Type) -> None:
    if not name in obj:
        raise KeyError(f"Missing required field '{'.'.join(path)}.{name}'")
    if not isinstance(obj[name], field_type):
        raise ValueError(
            f"Field '{'.'.join(path)}.{name}' must be a {field_type.__name__}"
        )


def __validate_section(section: dict, section_idx) -> None:
    __validate_field(section, ["sections"], "name", str)
    __validate_field(section, ["sections"], "description", str)
    __validate_field(section, ["sections"], "fields", list)

    for idx, field in enumerate(section["fields"]):
        __validate_field(field, [f"sections[{section_idx}]", f"fields[{idx}]"], "id", str)
        __validate_field(field, [f"sections[{section_idx}]", f"fields[{idx}]"], "label", str)
        __validate_field(field, [f"sections[{section_idx}]", f"fields[{idx}]"], "type", str)
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

    files: list[str]
    """The files that the template should apply to"""

    sections: list[Section]
    """Sections for the wizard of the template"""

    def get_directory(self) -> Path:
        """Get the directory where the template is stored

        :return: The directory
        """
        template_directory = Path.home() / ".captura" / "templates"

        # Change on linux to use the XDG Base Directory Specification
        if sys.platform == "linux" or sys.platform == "linux2":
            from xdg.BaseDirectory import xdg_data_dirs

            template_directory = Path(xdg_data_dirs[0]) / "captura" / "templates"
        return template_directory / f"{self.id}-{self.version}"


def config_from_yaml(yaml: dict) -> Config:
    """Create a config struct from a yaml dict

    :param yaml:
    :return: The config object
    """
    validate(yaml)
    return Config(**yaml)
