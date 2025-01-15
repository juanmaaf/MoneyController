FROM alpine:latest

RUN apk add --no-cache python3 py3-pip make curl bash

RUN adduser -D -h /home/test test

WORKDIR /app/test

ENV PATH="/home/test/.local/bin:$PATH"

USER test

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN mkdir -p /home/test/.cache && chmod -R a+w /home/test/.cache

RUN mkdir -p /home/test/.local/share/uv && chmod -R a+w /home/test/.local/share

ENV UV_CACHE_DIR=/home/test/.cache/uv

ENTRYPOINT ["make", "test"]