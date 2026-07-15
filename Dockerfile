FROM python:3.12-slim-bookworm
WORKDIR /app
COPY pyproject.toml README.md ./
COPY gateway ./gateway
COPY gateway_model ./gateway_model
RUN pip install --no-cache-dir . && useradd --create-home --uid 10001 gateway
USER 10001
EXPOSE 8000
CMD ["uvicorn", "gateway.main_v4:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
