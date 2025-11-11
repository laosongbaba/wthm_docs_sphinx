# WTHM IoT设备文档多语言实现方案

## 项目目标
实现WTHM IoT设备文档的中英文双语版本，托管在Read the Docs平台上，并通过RTD的翻译功能实现页面间语言切换。

## 最终实现方案

### 1. 项目结构
```
wthm_docs_sphinx/
├── docs/
│   ├── conf.py
│   ├── index.rst  # 主页（包含欢迎内容和导航）
│   ├── main.rst  # 欢迎页面
│   ├── product-specs.rst  # 产品规格
│   ├── panel-operations.rst  # 面板操作
│   ├── wifi-config.rst  # WiFi配置
│   ├── detailed-instructions.rst  # 详细说明
│   ├── zh_main.rst  # 中文欢迎页面内容
│   ├── zh_product-specs.rst  # 中文产品规格内容
│   ├── zh_panel-operations.rst  # 中文面板操作内容
│   ├── zh_wifi-config.rst  # 中文WiFi配置内容
│   ├── zh_detailed-instructions.rst  # 中文详细说明内容
│   ├── en_main.rst  # 英文欢迎页面内容
│   ├── en_product-specs.rst  # 英文产品规格内容
│   ├── en_panel-operations.rst  # 英文面板操作内容
│   ├── en_wifi-config.rst  # 英文WiFi配置内容
│   ├── en_detailed-instructions.rst  # 英文详细说明内容
│   └── _static/images/  # 图片资源（中英文共享）
├── IMPLEMENTATION.md  # 实现方案文档
├── .readthedocs.yaml
├── requirements.txt
└── build_docs.sh      # 本地构建脚本
```

### 2. 语言实现机制
- 使用Sphinx的`ifconfig`指令根据`READTHEDOCS_LANGUAGE`环境变量判断当前语言
- 在每个标准命名的RST文件中使用条件指令显示对应语言内容
- 所有图片资源在`_static/images/`目录中对中英文版本共享

### 3. 具体实现方式

**主页（index.rst）：**
```rst
.. ifconfig:: language == 'zh_CN'

   欢迎
   ====

   .. include:: zh_main.rst

.. ifconfig:: language != 'zh_CN'

   Welcome
   =======

   .. include:: en_main.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   self
   product-specs
   panel-operations
   wifi-config
   detailed-instructions
```

**其他页面（如main.rst）：**
```rst
|main_title|
============

.. ifconfig:: language == 'zh_CN'
   
   .. include:: zh_main.rst

.. ifconfig:: language != 'zh_CN'
   
   .. include:: en_main.rst
```

### 4. Sphinx配置（conf.py）
- 根据`READTHEDOCS_LANGUAGE`环境变量设置`language`参数
- 通过`rst_epilog`定义语言特定的替换变量
- 语言相关的项目信息（如项目名）根据语言环境动态设置

### 5. RTD配置
- 在RTD平台上创建两个项目（中英文）
- 设置翻译关系，使两个项目相互关联
- 用于语言切换功能

### 6. 语言切换实现
- RTD内置的翻译切换功能可正常工作
- 访问`/zh-cn/latest/`显示中文版，`/en/latest/`显示英文版
- 右下角语言切换按钮可在两个版本间切换

### 7. 特殊处理
- 主页（index.rst）直接显示欢迎内容，访问根URL时直接看到主内容
- 左侧导航目录根据语言正确显示内容，无重复现象
- PDF版本中无重复章节问题

### 8. 维护和使用说明
- **推荐构建方式**：使用Read the Docs平台远程构建，无需本地构建
- **内容更新**：修改`zh_*.rst`和`en_*.rst`文件以更新中英文内容
- **图片共享**：所有图片在`_static/images/`目录共享，RST文件使用`/_static/images/`路径引用
- **自动部署**：推送代码后RTD自动构建并发布新版本
- **导航结构**：标准命名的RST文件（main.rst等）作为入口，语言特定内容在zh_*.rst/en_*.rst中
- **PDF生成**：配置已优化，避免索引和重复章节问题
- **本地构建**：使用`build_docs.sh`脚本进行本地构建和预览
  - `./build_docs.sh` 或 `./build_docs.sh zh/cn/chinese` - 构建中文版本（默认）
  - `./build_docs.sh en/english` - 构建英文版本
  - `./build_docs.sh all` - 构建中英文两个版本
- **本地预览**：构建完成后，可通过以下方式预览
  - **直接打开文件**：在浏览器中打开对应HTML文件
    - 中文版：`docs/_build/html_zh/index.html`
    - 英文版：`docs/_build/html_en/index.html`
    - 两个版本：同时生成在上述两个目录中
  - **HTTP服务器方式**（适用于无GUI环境或需要远程访问）：
    1. 进入对应构建目录：`cd docs/_build/html_zh` 或 `cd docs/_build/html_en`
    2. 启动HTTP服务器：`python3 -m http.server 8000`
    3. 在浏览器中访问：`http://<服务器地址>:8000`

### 9. 项目特点
- **多语言共享代码库**：中英文在同一仓库维护
- **自动语言检测**：基于RTD环境变量自动切换语言
- **图片资源共享**：同一图片资源供中英文使用
- **标准Sphinx流程**：符合Sphinx文档标准
- **RTD集成**：与Read the Docs平台完全集成

此实现方案既保持了中英文内容的独立性，又能与RTD的翻译机制良好兼容，实现了预期的所有功能。