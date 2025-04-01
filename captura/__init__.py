"""The Captura Main Module

This module contains the main entry point for the Captura application.

Captura is a templating program, that allows you to fill out LaTeX templates
from a predefined template and generate different kinds of LaTeX documents.
Due to its modular design, it is easily extensible with new templates."""

__version__: str = "0.1.0"
"""The current version of the Captura application."""

production: bool = False
"""Indicates whether the application is running in production mode or development mode."""

environment: str = "linux"
"""The current environment in which the application is running.

This can be `linux`, `windows`, or `macos`."""
