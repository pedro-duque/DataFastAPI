FROM python:3.9

RUN pip install fastapi azure-storage-blob uvicorn starlette python-multipart

WORKDIR /app

COPY api/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
