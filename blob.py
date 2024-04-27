import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import time

class Blob:
    CONTAINER_NAME = 'jogos'
    
    def __init__(self):
        load_dotenv()
        self.blob_service_client = self.__get_blob_service_client_account_key()
        self.container_client = self.blob_service_client.get_container_client(Blob.CONTAINER_NAME)

    def __get_blob_service_client_account_key(self):
        # TODO: Replace <storage-account-name> with your actual storage account name
        account_url = os.getenv("AZURE_BLOB_URL")
        shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
        credential = shared_access_key

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=credential)

        return blob_service_client
    
    def download_folder(self, folder_path, local_directory):
        print('iniciou')

        inicio = time.time()
        blobs_list = self.container_client.list_blobs(name_starts_with=folder_path)

        for blob in blobs_list:
            # Crie o caminho do arquivo local
            local_file_path = os.path.join(local_directory, blob.name)
            # Crie diretórios necessários
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            with open(file=local_file_path, mode="wb") as download_file:
                download_file.write(self.container_client.download_blob(blob.name).readall())
        fim = time.time()

        print(f'Download concluido, decorrido: {(fim - inicio) / 60} em minutos')

    def upload_blob_file(self, file_name: str):
        name_blob = file_name.replace('./jogo/','')
        with open(file=file_name, mode="rb") as data:
            blob_client = self.container_client.upload_blob(name=name_blob, data=data, overwrite=True)
        
        print('finalizou o upload para o blob')
          

