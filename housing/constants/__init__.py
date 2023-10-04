import os,sys
from datetime import datetime

ROOT_DIR = os.getcwd() # To get the current working directory path

CONFIG_DIR = "config" # directory for config
CONFIG_FILE_NAME = "config.yaml"

# Join all the working directory together

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACTS_DIR_KEY = "artifact_dir"
print(CONFIG_FILE_NAME)
