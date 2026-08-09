FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
COPY gateway/ gateway/
RUN pip install --no-cache-dir fastapi uvicorn pydantic
EXPOSE 8000
CMD ["uvicorn", "gateway.api_v4_1:app", "--host", "0.0.0.0", "--port", "8000"]
