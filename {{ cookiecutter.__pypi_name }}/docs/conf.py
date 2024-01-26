# SPDX-FileCopyrightText: {% now 'utc', '%Y' %} {{ cookiecutter.author_name }}
# SPDX-License-Identifier: {{ cookiecutter.license }}

"""Configuration settings for sphinx."""

import sphinx_rtd_theme

project = "{{ cookiecutter.library_name }}"
copyright = "{% now 'utc', '%Y' %} {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), "_static"]
html_static_path = ["_static"]
