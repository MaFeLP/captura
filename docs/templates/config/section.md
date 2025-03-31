---
title: Sections
layout: default
---

# Sections in Templates

## `sections`
- **Type**: List of [`section` objects](#section-object)
- **Description**: Defines the different sections displayed in the template wizard. Each section groups related fields together
- **Example**: See subsections below

### Section Object
Each section in the `sections` array contains:

## `name`
- **Type**: String
- **Description**: The title of the section as displayed in the wizard
- **Example**: `"General Information"`

## `description`
- **Type**: String
- **Description**: A brief explanation of the section's purpose
- **Example**: `"General information about the document"`

## `fields`
- **Type**: Array of [`field` objects](#field-object)
- **Description**: Contains the input fields that will be shown within this section
- **Example**: See field objects below

### Field Object
Each field in the `fields` array must contain:

## `id`
- **Type**: String (alphanumeric with underscores)
- **Description**: A unique identifier for the field. Used as a variable name in Jinja2 when processing templates
- **Example**: `"title"`

## `label`
- **Type**: String
- **Description**: The display text shown next to the field in the wizard. Functions as a placeholder or prompt for the user
- **Example**: `"Titel"`

## `type`
- **Type**: [String (enum)](#field-types)
- **Description**: Determines the input type for the field
- **Allowed values**: `"text"`, `"checkbox"`, or `"list"`
- **Example**: `"text"`

### Field Types
#### Text Field
- Used for single-line text input
- **Example**: `"title"`, `"author"`, `"date"`

#### Checkbox
- Used for boolean values (true/false)
- **Example**: `"use_today"` for toggling the use of `\today` macro

#### List Field
- Used for collecting multiple values
- **Example**: `"keywords"` for entering multiple keywords

