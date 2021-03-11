FROM python:3.9-alpine
LABEL maintainer='https://www.github.com/agupta231'

RUN mkdir /src && pip install -U pip wheel setuptools && pip install requests

COPY cronjob /etc/crontabs/root
CMD ["crond", "-f", "-d", "8"]