FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

WORKDIR /bot

COPY .python-version pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .
