    # Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Blog da Miriam Yumi"
copyright = '2022, yumiriam'
author = 'yumiriam'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'ablog',
    'sphinx.ext.intersphinx',
    'sphinx_panels',
    'sphinxcontrib.icon'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "images/me.png"
html_title = "Miriam Yumi"
html_static_path = ['_static']

html_theme_options = {
    'navbar_align': 'left',
    'icon_links': [
        {
            'name': "GitHub",
            'url': "https://github.com/yumiriam",
            'icon': "fa-brands fa-github",
            'type': "fontawesome",
        },
        {
            'name': "LinkedIn",
            'url': "https://www.linkedin.com/in/miriam-yumi",
            'icon': "fa-brands fa-linkedin",
            'type': "fontawesome",
        },
#        {
#            'name': "Medium",
#            'url': "https://medium.com/@yumiriam",
#            'icon': "fa-brands fa-medium",
#            'type': "fontawesome",
#        },
        {
            'name': "Mastodon",
            'url': "https://indieweb.social/@yumiriam",
            'icon': "fa-brands fa-mastodon",
            'attributes': {
               "rel" : "me",
            }
        },
    ],
}

