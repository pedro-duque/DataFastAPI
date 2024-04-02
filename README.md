# FastAPI to interacts with an Azure Data Lake

This Python FastAPI project provides endpoints to interact with Azure Data Lake Storage (ADLS) for uploading, downloading, and listing files stored in ADLS containers.

## Features

- **Upload File**: Upload a file to ADLS.
- **Download File**: Download a file from ADLS.
- **List Files**: List all files in a specified container in ADLS.

## Installation

### Docker

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-directory>
```

3. Build the Docker image:

```bash
docker build -t adls-api .
```

4. Run the Docker container:

```bash
docker run -d -p 80:80 --env AZURE_STORAGE_CONNECTION_STRING="<your-connection-string>" adls-api
```

Replace `<your-connection-string>` with your Azure Storage account connection string.

## Usage

### Endpoints

- **Upload File**: `POST /upload-file`
  - Uploads a file to ADLS.
  - Example: `curl -X POST -F "file=@/path/to/file" http://localhost/upload-file`

- **Download File**: `GET /download-file/{filename}`
  - Downloads a file from ADLS.
  - Example: `http://localhost/download-file/{filename}`

- **List Files**: `GET /list-files/{container}`
  - Lists all files in a specified container in ADLS.
  - Example: `http://localhost/list-files/{container}`

### Environment Variables

- `AZURE_STORAGE_CONNECTION_STRING`: Azure Storage account connection string.

## Dependencies

- `fastapi`: FastAPI framework for building APIs with Python.
- `azure-storage-blob`: Azure Blob Storage client library for Python.
- `uvicorn`: ASGI server for running FastAPI applications.
- `starlette`: ASGI framework for building high-performance web services.
- `python-multipart`: Library for parsing multipart/form-data in Python.

## Configuration

Before running the application, ensure you set the `AZURE_STORAGE_CONNECTION_STRING` environment variable with your Azure Storage account connection string.

## Logging

This project uses Python's built-in `logging` module for logging informational messages.

## Note

Ensure that you have the necessary permissions and configurations set up in your Azure environment to access Azure Data Lake Storage.
