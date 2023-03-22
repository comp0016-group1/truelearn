# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import inspect
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "TrueLearn"
# pylint: disable=redefined-builtin
copyright = "2023, TrueLearn"
author = "TrueLearn Team"


# pylint: disable=wrong-import-position
import truelearn

version = truelearn.__version__
release = truelearn.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.linkcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for autodoc extension -------------------------------------------
autodoc_mock_imports = ["trueskill", "sklearn", "mpmath"]

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "mpmath": ("https://mpmath.org/doc/current/", None),
    "trueskill": ("https://trueskill.org/", None),
}


# -- Options for linkcode extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html
# Code below from:
# https://github.com/Lasagne/Lasagne/blob/master/docs/conf.py#L114


def linkcode_resolve(domain, info):
    """Determine the URL corresponding to the sourcecode."""

    def find_source():
        # Find the file and line number, based on code from numpy:
        # https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L286

        obj = sys.modules[info["module"]]
        for part in info["fullname"].split("."):
            obj = getattr(obj, part)
        fn = inspect.getsourcefile(obj)
        if fn is not None:
            fn = os.path.relpath(fn, start=os.path.dirname(truelearn.__file__))
        source, lineno = inspect.getsourcelines(obj)
        return fn, lineno, lineno + len(source) - 1

    if domain != "py" or not info["module"]:
        return None
    try:
        source_info = find_source()
        filename = f"truelearn/{source_info[0]}#L{source_info[1]}-L{source_info[2]}"
    except Exception:
        filename = info["module"].replace(".", "/") + ".py"
    tag = "main" if "dev" in version else "v" + version
    return f"https://github.com/comp0016-group1/truelearn/blob/{tag}/{filename}"


sphinx_gallery_conf = {
    "reference_url": {
        # The module you locally document uses None
        "truelearn": None,
    },
    "examples_dirs": "../examples",  # path to your example scripts
    "gallery_dirs": "examples",  # path to where to save gallery generated output,
    "download_all_examples": False,  # disable download file buttons
    "remove_config_comments": True,
    "show_memory": False,
    "show_signature": False,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Install furo theme with pip install furo
html_theme = "furo"

# See GitHub issue : https://github.com/readthedocs/readthedocs.org/issues/1776
html_static_path = ["_static"]

html_css_files = ["custom.css"]
