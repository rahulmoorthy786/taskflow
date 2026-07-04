FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN  pip install --no-cache-dir  -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python","run.py"]
