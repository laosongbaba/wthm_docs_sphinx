# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD  ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

# Define language-specific source directories
ZHSOURCEDIR   = $(SOURCEDIR)/zh
ENSOURCEDIR   = $(SOURCEDIR)/en

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile zh en

# Build Chinese documentation
zh:
	@$(SPHINXBUILD) -M html "$(ZHSOURCEDIR)" "$(BUILDDIR)/zh" $(SPHINXOPTS) -D language='zh_CN'

# Build English documentation
en:
	@$(SPHINXBUILD) -M html "$(ENSOURCEDIR)" "$(BUILDDIR)/en" $(SPHINXOPTS) -D language='en'

# Catch-all target: route all unknown targets to Sphinx-build
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)