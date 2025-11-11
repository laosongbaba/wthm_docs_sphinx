# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

# Determine language based on RTD environment or environment variable
import os

# First, check if we're on RTD and try to determine from the language subdomain
rtd_language = os.environ.get('READTHEDOCS_LANGUAGE', None)
env_language = os.environ.get('SPHINX_LANGUAGE', None)

if env_language:
    # Use environment variable if set
    language_env = env_language
elif rtd_language:
    # Use RTD language if available
    language_env = rtd_language
else:
    # Default fallback
    language_env = 'zh_CN'

if language_env.startswith('en'):
    project = 'WTHM IoT Device Documentation'
    copyright = '2025, Monigear'
    author = 'Monigear'
    language = 'en'
    # Define replacement variables for English
    rst_epilog = """
.. |main_title| replace:: WTHM IoT Device Documentation
.. |welcome_title| replace:: Welcome
.. |product_specs_title| replace:: Product Specifications
.. |panel_ops_title| replace:: Panel Operations
.. |wifi_config_title| replace:: Wi-Fi Configuration
.. |detailed_instr_title| replace:: Detailed Instructions
"""
    # In this approach, we don't exclude files as we use standard names with conditional includes
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
else:
    project = 'WTHM IoT设备文档'
    copyright = '2025, Monigear'
    author = 'Monigear'
    language = 'zh_CN'
    # Define replacement variables for Chinese
    rst_epilog = """
.. |main_title| replace:: WTHM IoT设备文档
.. |welcome_title| replace:: 欢迎
.. |product_specs_title| replace:: 产品技术参数
.. |panel_ops_title| replace:: 液晶屏显示及按键说明
.. |wifi_config_title| replace:: Wi-Fi配网说明
.. |detailed_instr_title| replace:: Wi-Fi配网详细指引
"""
    # In this approach, we don't exclude files as we use standard names with conditional includes
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # For parsing markdown files
    'sphinx.ext.autosectionlabel',  # For linking to sections
    'sphinx.ext.ifconfig',  # For conditional content
]

# Also add 'only' directive support which is built-in but needs to be enabled for language-specific content
# No additional extension needed as 'only' is built-in

templates_path = ['_templates']

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
html_static_path = ['_static']

# Additional configuration for Read the Docs
html_logo = '_static/images/monigear.jpg'
html_favicon = '_static/images/favicon.ico'

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
    ('index', 'WTHM_IoT_Docs.tex', project,  # Use dynamic project name
     'Monigear', 'manual'),
]
