from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import Data_Ingestion_Config
import os, sys

class DataIngestion:

    def __init__(self, data_ingestion_config:Data_Ingestion_Config):
        try:
            logging.info(f"{'='*20} Data Ingestion Log Has Started.... {'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e
