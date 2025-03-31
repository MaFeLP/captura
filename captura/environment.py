import sys
from pathlib import Path

template_directory: Path = Path.home() / ".captura" / "templates"
"""The directory where templates are stored."""

# Change on linux to use the XDG Base Directory Specification
if sys.platform == "linux" or sys.platform == "linux2":
    from xdg.BaseDirectory import xdg_data_dirs

    template_directory = Path(xdg_data_dirs[0]) / "captura" / "templates"

if not template_directory.exists():
    template_directory.mkdir(parents=True)
