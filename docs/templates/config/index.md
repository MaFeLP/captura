---
title: The Template Configuration
layout: default
---

# The Template Configruation
The template configuration is split up into two parts: [Metadata]({% link metadata.md %}) about the template
and [Section]({% link section.md %}) where the different parts of the wizard are defined.

## Sample Configuration
```yaml
##############################
##         Metadata         ##
##############################

## The name of the template
name: "Example Template"

## A short description of the template
description: "An example template to illustrate how templates work"

## The id of the template in reverse DNS notation.
## This id has to be unique, as captura uses it to identify
## templates in the library and overrides the same templates.
id: "com.example.example_template"

## The version of the template
## Together with the id, the version is used to uniquely
## identify a template in the library of captura
version: "1.0.0"

## The main author of the template.
## ONLY accepts a string
author: "MaFeLP <mafelp@proton.me>"

## The license of the template
license: "CC0"

## tags of the template.
## A list of strings that might be used in the future to
## create a "template store"
tags: [ "example", "template" ]

## A list of LaTeX source code files that will be modified using Jinja2
## with the values filled out in the sections
files:
  - "index.tex"

## If the template only consists of one file or multiple files.
## If this value is true, when the wizard finishes it will ask for a file save path and will not keep the original filename.
## If this value is false, the wizard will ask for a directory to save the files to and keep the original filenames.
single_file: true

##############################
##         Sections         ##
##############################
sections:
  ## Each section has a 'name', a 'description' and 'fields'

  - name: "General Information"  # The name of the section, as displayed in the wizard
    description: "General information about the document"  # A short description for the current section

    fields:
      ## Each field has to have the three attributes 'id', 'label', and 'type'
      - id: "title"  # an alphanumerical (and '_') and unique value. This id represents a value in Jinja2, when using a template
        label: "Titel"  # The placeholder text displayed in the wizard
        type: "text"  # Can be either of 'text', 'checkbox', or 'list'

      - id: "author"
        label: "Author"
        type: "text"

      - id: "use_today"
        label: "Use '\\today' as the current date?"
        type: "checkbox"

      - id: "date"
        label: "Datum"
        type: "text"

      - id: "keywords"
        label: "Additional Keywords"
        type: "list"

  - name: "Macros"
    description: "Additional makros for the "
    fields:
      - id: "mkline"
        label: "mkline — Eine horizontale Linie erstellen"
        type: "checkbox"
```

## Sample `index.tex` file for the config above
```tex
\documentclass{article}
\usepackage{lipsum}

\title{ {{- title -}} }
\author{ {{- author -}} }
{% if use_today %}
\date{\today}
{% else %}
\date{ {{- date -}} }
{% endif %}

{% if mkline %}
\newcommand{\mkline}{\begin{center}\line{0.4\lineheight}{.5\textwidth}}
{% endif %}

\begin{document}

\maketitle

\section{Keywords of the Document}
\begin{itemize}
{% for keyword in keywords %}
  \item {{ keyword }}
{% endfor %}
\end{itemize}

\lipsum

\end{document}
```

