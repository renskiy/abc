FROM python:3.7-slim

WORKDIR /opt/abc

COPY requirements.docker.txt .

RUN set -ex \
    && apt-get update \
# install build dependencies
    && apt-get install -y --no-install-recommends \
        gcc \
        libpcre3 \
        libpcre3-dev \
    && rm -rf /var/lib/apt/lists/* \
# install project requirements
    && pip install --no-cache-dir --requirement requirements.docker.txt \
# remove build dependencies
    && apt-get autoremove -y gcc libpcre3-dev

COPY . .

RUN ./manage.py collectstatic

EXPOSE 8080

ENV UWSGI_PROTOCOL=http UWSGI_PROCESSES=2 HTTP_SOCKET=:8080

CMD ["uwsgi", "--ini", "uwsgi.ini"]
