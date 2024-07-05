# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'plenoptic tutorial, CSHL Vision Course, 2024'
copyright = '2024, Billy Broderick'
author = 'Billy Broderick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# max time (in secs) per notebook cell. here, we disable this
nb_execution_timeout = -1
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/plenoptic.ico'
html_sourcelink_suffix = ""
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/LabForComputationalVision/plenoptic-cshl-vision-2024",
    "repository_url": "https://github.com/LabForComputationalVision/plenoptic-cshl-vision-2024",
    "logo": {
        "alt_text": "Home",
        "image_light": "_static/plenoptic.svg",
        "image_dark": "_static/plenoptic_darkmode.svg",
    },
    "use_download_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://binder.flatironstitute.org/~wbroderick/cshl2024",
        "notebook_interface": "jupyterlab",
    },
    "article_footer_items": ["last-updated", "execute"],
}
