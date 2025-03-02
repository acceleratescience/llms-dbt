FROM python:3.12-slim

# Install basic dev tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -ms /bin/bash vscode
USER vscode

# Set working directory
WORKDIR /workspaces

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Upgrade pip
RUN pip install --upgrade pip