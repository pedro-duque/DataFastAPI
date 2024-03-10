from logging import exception
import logging
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse
from io import StringIO, BytesIO
import os
from azure.storage.blob import BlobServiceClient, BlobClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

app = FastAPI()

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    # Extraia a extensão do arquivo
    filename, extension = os.path.splitext(file.filename)

    # Conecte-se ao Data Lake Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURE_STORAGE_CONNECTION_STRING"))

    # Crie um container para os arquivos
    container_client = blob_service_client.get_container_client(f"{extension.lstrip('.')}-data")

    # Carregue o arquivo para o container
    container_client.upload_blob(file.filename, file.file, overwrite=True)
    
    return {"message": "Arquivo carregado com sucesso",
            "path": file.filename
            }

@app.get("/download-file/{filename}")
async def download_file(filename: str):
    # Extraia a extensão do arquivo
    fullname = filename
    filename, extension = os.path.splitext(filename)

    # Conecte-se ao Data Lake Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURE_STORAGE_CONNECTION_STRING"))

    # Obtenha o container para os arquivos
    container_client = blob_service_client.get_container_client(f"{extension.lstrip('.')}-data")

    # Baixe o arquivo do container
    blob_downloader = container_client.download_blob(fullname).readall()
    bytes_io = BytesIO(blob_downloader)


    response = StreamingResponse(bytes_io)
    response.headers["Content-Disposition"] = f"attachment; filename={fullname}"
    response.headers["Content-Type"] = "application/octet-stream"

    return response

@app.get("/list-files/{container}")
async def list_files(container: str):
    # Conecte-se ao Data Lake Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURE_STORAGE_CONNECTION_STRING"))
    logger.info("Lendo container:", container)
    # Obtenha o container para os arquivos CSV
    container_client = blob_service_client.get_container_client(container)

    # Liste os arquivos no container
    blobs = container_client.list_blobs()

    return {"files": [blob.name for blob in blobs]}