from housing.entity.config_entity import *
from utils.utils import read_yaml_file
from housing.constants import *
from housing.exception import HousingException
import os, sys
from housing.logger import logging


ROOT_DIR
class configuration:

    def __init__(
            self,
            config_file_path:str = CONFIG_FILE_PATH,
            current_time_stamp:str =CURRENT_TIME_STAMP
            ):
        
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.time_stamp = current_time_stamp
        self.training_pipeline_config = self.get_training_pipeline_config()

    def get_data_ingestion_config(self) -> Data_Ingestion_Config: # for data ingestion
        pass

    def get_data_validation_config(self) -> Data_Validation_Config: # for data validation
        pass

    def get_data_transformation_config(self) -> Data_Transformation_Config: # for data transformation
        pass

    def get_model_training_config(self) -> Model_Trainer_Config: # for model training
        pass

    def get_model_evaluation_config(self) -> Model_Evaluation_Config: # for model evaluation
        pass

    def get_model_pusher_config(self) -> Model_Pusher_Config: # for model pushing or deployment
        pass

    def get_training_pipeline_config(self) -> Training_Pipeline_Config: # for training
        try:
            training_pipeline_config_key = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifacts_dir = os.path.join(ROOT_DIR, 
                                         training_pipeline_config_key[TRAINING_PIPELINE_NAME_KEY],
                                         training_pipeline_config_key[TRAINING_PIPELINE_ARTIFACTS_DIR_KEY]
                                         )
            training_pipeline_config = Training_Pipeline_Config(artifacts_dir=artifacts_dir)
            logging.info(f"Training Pipeline Config {training_pipeline_config}")
            return training_pipeline_config 
        except Exception as e:
            raise HousingException(e, sys) from e
