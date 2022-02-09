# List the pdf's to build. foo.tex will produce foo.pdf
TARGETS = en.subject.pdf

# List the files included in the slides
DEPS = en.ex02_interlude.tex  en.ex03_interlude.tex  en.ex06_interlude.tex  en.ex08_interlude.tex  en.py_proj.tex  en.subject.tex  usefull_ressources.tex

# Relative path to the LaTeX documentclass setup files
# Adapt as needed
# RELPATH = $(shell git rev-parse --show-toplevel)/resources/latex/
# RELPATH for github actions:
RELPATH = $(shell $(dirname `pwd`))/resources/latex/

# You should not touch this either
include $(RELPATH)/Makefile.LaTeX
