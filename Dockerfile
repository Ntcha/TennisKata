FROM debian:bullseye

RUN apt-get update
RUN apt-get install -y python3.7 python3-pip
RUN ln -s /usr/bin/python3.7 /usr/bin/python
RUN python -m pip install pytest
