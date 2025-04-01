---
title: Template Creation
layout: default
---

# Template Creation

{: .note }
Before creating your first template, it is recommended you are familiar with
[Jinja2] as it is the templating
language used by Captura.

A template consists of three parts:

1. A `config.yml` file, that defines the behavior of the wizard. See [config] for more options on the config file.
2. An optional `template.png` file that is shown as a preview on the homepage of the application.
3. A folder `files/` that holds the LaTeX files for the template.

## Creating a Template
1. Create a new folder for your template.
2. Create a new sub-folder `files/` in that folder, as well as a [config] file.
3. Add the needed LaTeX Source files in the `files/` folder.
4. Create a ZIP Archive of the **contents** of the folder. Inside the ZIP-Archive, the `config.yml`, `files/` and
   `template.png` should be at the top level of the archive!
5. Rename the ZIP-Archive to match the format `<TEMPLATE ID>-<TEMPLATE VERSION>`, e.g. `com.github.mafelp.captura.mla_essay-1.0.0`
6. Change the file extension of the ZIP-Archive to be `.captura`, so that captura recognizes this filetype.

Alternatively you can also use the following script to bootstrap a template:

```bash
# Create the basic directory structure
mkdir -p "com.example.test_template/files/"
cd com.example.test_template

# Create an empty configuration file
touch config.yml

# Create a ZIP/Captura-Archive with all the files in the current directory
zip -r ../com.example.test_template-1.0.0.captura .
```

[config]: {% link templates/config/index.md %}
[Jinja2]: https://jinja.palletsprojects.com/en/stable/