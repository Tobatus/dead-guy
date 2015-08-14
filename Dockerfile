FROM centos:7

MAINTAINER Toba email: tommi.berg@elisa.fi

RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y update
RUN yum install -y python
RUN yum install -y python-pip
RUN pip install Tornado-JSON

COPY app.sh /var/app/
COPY app.cfg /var/app/
COPY app /var/app/app

EXPOSE 8888

CMD /var/app/app.sh
