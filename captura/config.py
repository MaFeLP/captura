import logging
from dataclasses import dataclass
from typing import Type

logger = logging.getLogger(__name__)


def __validate_field(obj: dict, path: list[str], name: str, field_type: Type) -> None:
    if not name in obj:
        raise KeyError(f"Missing required field '{'.'.join(path)}.{name}'")
    if not isinstance(obj[name], field_type):
        raise ValueError(
            f"Field '{'.'.join(path)}.{name}' must be a {field_type.__name__}"
        )


def __validate_section(section: dict) -> None:
    __validate_field(section, ["sections"], "name", str)
    __validate_field(section, ["sections"], "description", str)
    __validate_field(section, ["sections"], "fields", list)

    for idx, field in enumerate(section["fields"]):
        __validate_field(field, ["sections", f"[{idx}]"], "id", str)
        __validate_field(field, ["sections", f"[{idx}]"], "label", str)
        __validate_field(field, ["sections", f"[{idx}]"], "type", str)
        for char in field["id"]:
            if not char.isalnum():
                raise ValueError(
                    f"Field 'sections.[{idx}].id' contains invalid characters"
                )
        if not field["type"] in ["text", "checkbox", "select"]:
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

    logger.debug("Top Level fields are valid")

    for section in config["sections"]:
        __validate_section(section)


@dataclass
class Field:
    """A specific field of a section"""

    id: str
    """The id of the field, will be the variable name in the template"""

    label: str
    """The label of the field, will be shown in the wizard to the use"""

    type: str
    """The type of the field, can be 'text', 'checkbox' or 'select'"""


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


def config_from_yaml(yaml: dict) -> Config:
    """Create a config struct from a yaml dict

    :param yaml:
    :return: The config object
    """
    validate(yaml)
    return Config(**yaml)
