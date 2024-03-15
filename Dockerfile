FROM python:3.9

ENV AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=devpedroduque;AccountKey=aarKW4123wJWJQs7sF8dJpV2fifgRQwbbMwNyYk6BRBvtAyzfJZM2ChQ+o7xypiVoeCrA/b5kXmB+AStyGNMFw==;EndpointSuffix=core.windows.net"

RUN pip install fastapi azure-storage-blob uvicorn starlette python-multipart

WORKDIR /app

COPY api/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]