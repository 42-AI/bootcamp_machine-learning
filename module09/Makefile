# List the pdf's to build. foo.tex will produce foo.pdf
TARGETS = en.subject.pdf

# List the files included in the slides
DEPS = exercises/en.ex01_interlude.tex \
	exercises/en.ex04_interlude.tex \
	exercises/en.ex06_interlude.tex \
	exercises/en.ex08_interlude.tex \
	exercises/en.ex10_interlude.tex \
	../resources/42ai_bootcamps/en.instructions.tex \
	../resources/42ai_bootcamps/en.acknowledgements.tex \
	useful_resources.tex

# Relative path to the LaTeX documentclass setup files
# Adapt as needed
# RELPATH = $(shell git rev-parse --show-toplevel)/resources/latex/
# RELPATH for github actions:
RELPATH = $(shell dirname `pwd`)/resources/latex/

# You should not touch this either
include $(RELPATH)/Makefile.LaTeX
