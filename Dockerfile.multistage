# Build Stage 

FROM python:3.12-alpine  AS builder

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

RUN chown -R appuser:appgroup /app

USER appuser

COPY . .

# Runner Stage

FROM python:3.12-slim  AS runner

WORKDIR /app

COPY requirements.txt  .

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

RUN pip install --upgrade pip

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python","run.py"]
