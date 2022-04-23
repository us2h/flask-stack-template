FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN set -eux \
    pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/
WORKDIR /app

EXPOSE 80
CMD ["gunicorn", "--timeout", "300", "--workers", "4", "--bind", "0.0.0.0:80", "app:app"]