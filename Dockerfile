# ---------- Builder Stage ----------
FROM python:3.12-alpine AS builder

WORKDIR /app

# Create non-root user and virtual environment
RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir \
    --root-user-action=ignore \
    -r requirements.txt

# Copy application source
COPY . .

# Set ownership
RUN chown -R appuser:appgroup /app /opt/venv

USER appuser

# ---------- Runtime Stage ----------
FROM python:3.12-slim AS runner

WORKDIR /app

# Create the same non-root user
RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser

ENV PATH="/opt/venv/bin:$PATH"

# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv

# Copy application
COPY --from=builder /app /app

# Fix permissions
RUN chown -R appuser:appgroup /app /opt/venv

USER appuser

EXPOSE 5000

CMD ["python", "run.py"]