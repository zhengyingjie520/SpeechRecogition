FROM ubuntu:20.04
MAINTAINER qiyuan
COPY autosub /home/share/lmcproject/Task_one/autosub
COPY tomcat/apache-tomcat-8.5.69.tar.gz /usr/local/apache-tomcat-8.5.69.tar.gz
ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list \
	&& apt-get update --fix-missing && apt-get install -y software-properties-common openjdk-8-jdk vim python3-pip ffmpeg imagemagick --fix-missing \
	&& pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install -r /home/share/lmcproject/Task_one/autosub/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
	&& tar -zxvf /usr/local/apache-tomcat-8.5.69.tar.gz && chmod 755 -R apache-tomcat-8.5.69
COPY tomcat/sr.war /usr/local/apache-tomcat-8.5.69/webapps/sr.war
COPY tomcat/startup.sh /usr/local/apache-tomcat-8.5.69/bin/startup.sh
EXPOSE 8080
