FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY main.py .

# Install dependencies
RUN uv sync

# Expose the default port
EXPOSE 9000

# Start the MCP server
CMD ["uv", "run", "main.py"]
