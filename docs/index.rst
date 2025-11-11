.. WTHM Documentation master file
   This file will be dynamically adjusted based on the language

.. ifconfig:: language == 'zh_CN'

   欢迎
   ====

   .. include:: zh_main.rst

   .. toctree::
      :maxdepth: 2
      :caption: 目录:

      product-specs
      panel-operations
      wifi-config
      detailed-instructions

.. ifconfig:: language != 'zh_CN'

   Welcome
   =======

   .. include:: en_main.rst

   .. toctree::
      :maxdepth: 2
      :caption: Contents:

      product-specs
      panel-operations
      wifi-config
      detailed-instructions

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`