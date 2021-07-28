FROM ubuntu:20.04
MAINTAINER qiyuan
COPY autosub /home/share/lmcproject/Task_one/autosub
ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list \
	&& apt-get update --fix-missing && apt-get install -y openjdk-8-jdk vim python3-pip --fix-missing \
	&& pip3 install --upgrade pip \
