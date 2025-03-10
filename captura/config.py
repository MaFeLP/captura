import logging
from typing import Any, Type

logger = logging.getLogger(__name__)


def __validate_field(obj: Any, path: list[str], name: str, type: Type) -> None:
    if not name in obj:
        raise KeyError(f"Missing required field '{'.'.join(path)}.{name}'")
    if not isinstance(obj[name], type):
        raise ValueError(f"Field '{'.'.join(path)}.{name}' must be a {type.__name__}")


def __validate_section(section: Any) -> None:
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


def validate(config: Any) -> None:
    logger.debug("Validating configuration")
    for string in ["name", "description", "id", "version", "author", "license"]:
        __validate_field(config, [], string, str)

    for l in ["files", "tags", "sections"]:
        __validate_field(config, [], l, list)

    logger.debug("Top Level fields are valid")

    for section in config["sections"]:
        __validate_section(section)
