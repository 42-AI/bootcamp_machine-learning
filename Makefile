DIRECTORIES = 	module05 \
				module06 \
				module07 \
				module08 \
				module09

TARGETS_DIRS = $(DIRECTORIES:%=%/en.subject.pdf)

TARGETS = 	$(DIRECTORIES:%=%.pdf)

all: clean dirs

%.pdf: 
	@$(MAKE) -C `dirname $@`
	@$(MAKE) clean -C `dirname $@`
	cp $@ build/`dirname $@`.pdf

dirs: $(TARGETS_DIRS)

build_pdfs:
	sudo docker run -v "$(shell pwd)/build:/data/bootcamp_machine-learning/build" -i latex_build make

build_builder:
	sudo docker build -t latex_build .

clean:
	rm -rf $(TARGETS) $(TARGETS_DIRS)

debug:
	echo $(TARGETS_DIRS)
