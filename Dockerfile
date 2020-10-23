FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt update
RUN apt install -y curl python3 python3-pip
RUN pip3 install mtgsdk
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN export DEBIAN_FRONTEND=noninteractive && apt install -y postgresql
COPY ./ /app
WORKDIR /app
# CMD python3 setup.py
