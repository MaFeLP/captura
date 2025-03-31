---
title: Metadata
layout: default
parent: Configuration
---

# Template Metadata
Each template has a metadata section.

## `name`
- **Type**: String
- **Description**: The display name of the template shown to users in the interface
- **Example**: `"Example Template"`

## `description`
- **Type**: String
- **Description**: A brief explanation of the template's purpose and functionality
- **Example**: `"An example template to illustrate how templates work"`

## `id`
- **Type**: String (reverse DNS notation)
- **Description**: A unique identifier for the template using reverse DNS notation. Used by the system to identify templates in the library and handle overrides
- **Example**: `"com.example.example_template"`

## `version`
- **Type**: String (semantic versioning)
- **Description**: The version number of the template, following semantic versioning Combined with the ID, creates a unique identifier for the template in the library
- **Example**: `"1.0.0"`

## `author`
- **Type**: String
- **Description**: The main creator or maintainer of the template, optionally with contact information
- **Example**: `"MaFeLP <mafelp@proton.me>"`

## `license`
- **Type**: String
- **Description**: The license under which the template is released, indicating usage permissions
- **Example**: `"CC0"`

## `tags`
- **Type**: Array of Strings
- **Description**: A list of keywords that categorize the template. May be used for filtering or searching in a future "template store" implementation
- **Example**: `[ "example", "template" ]`

## `files`
- **Type**: Array of Strings
- **Description**: A list of LaTeX source code files that will be processed using Jinja2 templating. These files will be modified with values from the sections
- **Example**: `[ "index.tex" ]`

## `single_file`
- **Type**: Boolean
- **Description**: Determines how the wizard handles file saving
    - If `true`: Prompts for a single file save path and does not preserve the original filename
    - If `false`: Prompts for a directory and preserves the original filenames
- **Example**: `true`

