import os
import sys

# # Django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
# import django  # noqa
# django.setup()


# Path to the directory containing the Django project directory (mynhanes)
django_project_dir = os.path.abspath('../mynhanes')
sys.path.insert(0, django_project_dir)

# Django Settings
# Making sure we are pointing to the correct settings module
# within the 'project' folder
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
import django  # noqa
django.setup()


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyNHANES'
copyright = '2024, Andre Rico'
author = 'Andre Rico'
release = '0.2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx estensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
html_static_path = ['_static']
