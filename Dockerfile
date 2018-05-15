FROM python:latest
MAINTAINER "Serhii Kolesnikov" <serg220394@gmail.com>

RUN pip install psutil
WORKDIR util
ADD . /util
CMD ["python","script.py"]
