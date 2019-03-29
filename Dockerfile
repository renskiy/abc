FROM python:3.7-slim

WORKDIR /opt/abc

VOLUME /data

COPY requirements.docker.txt .

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpcre3 \
        libpcre3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --requirement requirements.docker.txt \
    && apt-get autoremove -y gcc libpcre3-dev

ENV UWSGI_PROTOCOL=http \
    UWSGI_PROCESSES=2 \
    UWSGI_SOCKET=:8000 \
    DJANGO_SETTINGS_MODULE=settings.docker

COPY . .

RUN set -ex \
    && pip install --no-cache-dir --upgrade pytz \
    && ./manage.py collectstatic

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
