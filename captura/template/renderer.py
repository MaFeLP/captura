import logging
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from captura.config import Config

logger = logging.getLogger(__name__)

SPECIAL_CHARACTERS = [
    ("\\", "\\textbackslash "),
    ("&", "\\&"),
    ("%", "\\%"),
    ("$", "\\$"),
    ("#", "\\#"),
    ("_", "\\_"),
    ("{", "\\{"),
    ("}", "\\}"),
    ("~", "\\textasciitilde "),
    ("^", "\\textasciicircum "),
]


def sanitize_single_value(value: any) -> any:
    if type(value) == str:
        for char, replacement in SPECIAL_CHARACTERS:
            value = value.replace(char, replacement)
    elif type(value) == list:
        for idx, item in enumerate(value):
            value[idx] = sanitize_single_value(item)
    return value


def sanitize_values(values: dict) -> dict:
    for key, value in values.items():
        values[key] = sanitize_single_value(value)
    return values


def render_all(path: Path, config: Config, values: dict) -> None:
    logger.info(f"Rendering template {config.id}-{config.version}")
    values = sanitize_values(values)

    env = Environment(
        loader=FileSystemLoader(config.get_directory() / "files"),
        autoescape=False,
    )

    if config.single_file:
        assert type(config.files[0]) == str, "Single file must be a string"
        logger.debug(f"Rendering single file {config.files[0]}...")
        string = env.get_template(config.files[0]).render(values)
        with open(path, "w") as f:
            f.write(string)
        return

    assert type(config.files) == list, "Multiple files must be a list"
    path.mkdir(parents=True, exist_ok=True)
    for file in config.files:
        logger.debug(f"Rendering file {file}...")
        string = env.get_template(file).render(values)
        with open(path / file, "w") as f:
            f.write(string)
    if config.assets:
        logger.debug("Copying assets...")
        for asset in config.assets:
            logger.debug(f"Copying asset {asset}...")
            shutil.copy(path / asset, path / asset)
