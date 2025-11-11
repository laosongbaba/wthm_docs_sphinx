# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

# Configuration for Chinese documentation
project = 'WTHM IoT设备文档'
copyright = '2025, Monigear'
author = 'Monigear'
language = 'zh_CN'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # For parsing markdown files
    'sphinx.ext.autosectionlabel',  # For linking to sections
]

templates_path = ['../_templates']

# Since we're in the zh subdirectory, exclude the en directory
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '../en/*']

# MyST configuration
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Use Read the Docs theme
html_static_path = ['../_static']

# Additional configuration for Read the Docs
html_logo = '../_static/images/th.png'
html_favicon = '../_static/images/th.png'

# Theme options for Read the Docs
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',  #  Provided by Google in your dashboard
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
\usepackage{charter}
\usepackage[defaultsans]{lato}
\usepackage{inconsolata}
% 设置图片不浮动，紧贴原文位置
\usepackage{float}
\let\oldfigure\figure
\renewenvironment{figure}[1][H]{\oldfigure[#1]}{\endoldfigure}
''',

    # Latex figure (float) alignment
    'figure_align': 'H',  # 使用 'H' 选项强制图片在确切位置放置

    # 去除多余的空白页
    'classoptions': ',openany,oneside',
    'babel': '\\usepackage[english]{babel}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'WTHM_IoT_Docs.tex', 'WTHM IoT设备文档',
     'Monigear', 'manual'),
]