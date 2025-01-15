FROM python:slim-bullseye

RUN apt-get update && apt-get install -y \
    make \
    curl \
    bash \
    && apt-get clean

WORKDIR /app/test

RUN adduser --disabled-password --gecos "" test

RUN mkdir -p /home/test/.cache && \
    chmod -R a+w /home/test/.cache

RUN mkdir -p /home/test/.venv && \
    chmod -R a+w /home/test/.venv

ENV PATH="/home/test/.local/bin:$PATH"

USER test

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/test/.cache/uv

ENTRYPOINT ["make", "test"]