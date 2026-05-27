import zipfile
import gdown
from cnnClassifier.utils.common import get_size
from cnnClassifier import logger
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
import os





class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)->str:

        try:
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_data_file  # ✅ convert once here
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading file from :[{dataset_url}] into :[{zip_download_path}]")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?export=download&id="
            gdown.download(url=prefix + file_id, output=str(zip_download_path), quiet=False)
            logger.info(f"Downloaded file size :[{get_size(zip_download_path)}]")

        except Exception as e:
            logger.error(f"Error occurred while downloading file: {e}")
            raise e

    def unzip_and_clean(self)->str:
        try:
            zip_download_path = self.config.local_data_file
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            logger.info(f"Unzipping file from :[{zip_download_path}] into :[{unzip_dir}]")
            with zipfile.ZipFile(zip_download_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            logger.info(f"Unzipped file size :[{get_size(unzip_dir)}]")
            
        except Exception as e:
            logger.error(f"Error occurred while unzipping file: {e}")
            raise e