FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

WORKDIR /bot

COPY .python-version pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .
