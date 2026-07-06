# ---------- Builder Stage ----------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ---------- Runtime Stage ----------
FROM python:3.12-slim

# Create a non-root user
RUN groupadd --system app && \
    useradd --system --gid app --create-home app

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

# Give ownership of application files
RUN chown -R app:app /app /opt/venv

# Switch to the non-root user
USER app

EXPOSE 5000

CMD ["python", "run.py"]