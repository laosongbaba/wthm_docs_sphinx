.. WTHM Documentation master file
   This file will be dynamically adjusted based on the language

.. ifconfig:: language == 'zh_CN'

   WTHM IoT设备文档
   ================

   .. toctree::
      :maxdepth: 2
      :caption: 目录:

      zh_main
      zh_product-specs  
      zh_panel-operations
      zh_wifi-config
      zh_detailed-instructions

.. ifconfig:: language == 'en' or language.startswith('en')

   Welcome to WTHM IoT Device Documentation!
   =========================================

   .. toctree::
      :maxdepth: 2
      :caption: Contents:

      en_main
      en_product-specs
      en_panel-operations
      en_wifi-config
      en_detailed-instructions

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`