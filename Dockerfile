FROM blang/latex:ubuntu

RUN pwd

COPY . /data/bootcamp_machine-learning

WORKDIR /data/bootcamp_machine-learning

RUN pwd

RUN make \
	&& ls -la . \
	&& ls -la module05

