import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv

class Blob:
    
    def __init__(self):
        load_dotenv()

    def get_blob_service_client_account_key(self):
        # TODO: Replace <storage-account-name> with your actual storage account name
        account_url = os.getenv("AZURE_BLOB_URL")
        shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
        credential = shared_access_key

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=credential)

        return blob_service_client
