FROM python:3.12-slim

# Copy the uv binary from its official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies first so Docker caches this layer
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev --no-install-project

# Then copy the application code
COPY app ./app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# 0.0.0.0 makes the server reachable from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]