FROM jupyter/base-notebook:latest
USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y git build-essential openssl python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev git-flow vim openjdk-8-jre
#ENV PATH $PATH:/home/jovyan/.local/bin
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com
WORKDIR /home/jovyan/work
