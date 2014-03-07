FROM ubuntu:quantal

# requirements

#RUN echo "deb http://ppa.launchpad.net/thumbor/ppa/ubuntu quantal main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C6C3D73D1225313B
RUN apt-get update
RUN apt-get install --force-yes -y ffmpeg libjpeg-dev libpng-dev libtiff-dev libjasper-dev libgtk2.0-dev python-dev python-numpy python-pycurl webp python-opencv python-pip python-imaging graphicsmagick curl vim
RUN pip install thumbor
RUN pip install redis

# service

#ENTRYPOINT thumbor
#USER daemon
EXPOSE 8888

ADD thumbor.conf /etc/thumbor.conf
