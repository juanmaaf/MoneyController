FROM alpine:latest

RUN apk add --no-cache python3 py3-pip make wget bash

RUN wget -qO- https://astral.sh/uv/install.sh | sh

WORKDIR /app/test

RUN adduser -D -h /home/usuarioNoPrivilegiado usuarioNoPrivilegiado

RUN mkdir -p /home/usuarioNoPrivilegiado/.cache/ && chmod -R a+w /home/usuarioNoPrivilegiado/.cache/

ENV UV_CACHE_DIR=/home/usuarioNoPrivilegiado/.cache/uv

USER usuarioNoPrivilegiado

ENTRYPOINT ["make", "test"]