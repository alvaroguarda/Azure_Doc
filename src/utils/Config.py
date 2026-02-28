import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("your_ENDPOINT_here")
    SUBSCRIPTION_KEY = os.getenv("your_SUBSCRIPTION_KEY_here")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("your_AZURE_STORAGE_CONNECTION_STRING_here")
    AZURE_STORAGE_CONTAINER_NAME = os.getenv("your_AZURE_STORAGE_CONTAINER_NAME_here")
