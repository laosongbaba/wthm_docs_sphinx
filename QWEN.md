## Qwen Added Memories
- WTHM文档项目的多语言实现方案总结：
1. 项目结构：使用标准文件名（main.rst, product-specs.rst等），通过条件指令显示不同语言内容
2. 语言切换：使用Sphinx的ifconfig指令，根据READTHEDOCS_LANGUAGE变量判断语言
3. 内容显示：在各页面使用ifconfig条件包含zh_*.rst或en_*.rst文件
4. 导航目录：index.rst中toctree不放在条件块内，避免重复显示
5. 主页显示：index.rst包含主页面内容，访问根URL直接显示欢迎内容
6. 图片共享：所有图片放在docs/_static/images/目录，供所有语言共享
7. RTD翻译：通过RTD项目设置建立中英文版本翻译关系
- WTHM文档项目开发过程中的重复错误：
1. 错误：在index.rst中使用多个ifconfig条件块定义toctree，导致左侧导航目录重复显示
2. 错误：使用only指令在某些RTD环境中导致内容不显示
3. 错误：使用rst_epilog替换变量但在页面内容中直接显示未解析的变量名
4. 解决方案：将toctree放在ifconfig条件块外，只保留一个toctree定义；使用ifconfig在页面内容中显示不同语言；避免直接在文本中使用未被正确处理的替换变量
- WTHM文档项目本地构建和预览：
1. 本地构建脚本：build_docs.sh（已删除不匹配的Makefile）
2. 构建命令：./build_docs.sh [zh|en|all]，支持中英文版本单独或同时构建
3. 本地预览：可直接打开HTML文件或使用python3 -m http.server 8000启动服务器进行预览
4. 构建输出：中文版在docs/_build/html_zh，英文版在docs/_build/html_en
5. 无GUI环境预览：在构建目录启动HTTP服务器，从客户端浏览器访问
