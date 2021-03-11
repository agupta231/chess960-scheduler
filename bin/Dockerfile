FROM python:3.9-alpine

RUN mkdir /scratch && cd /scratch

COPY requirements.txt .
RUN pip install -U pip wheel setuptools && pip install requests

COPY cronjob /etc/crontabs/root
CMD ["crond", "-f", "-d", "8"]