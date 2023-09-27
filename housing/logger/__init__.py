import logging
from datetime import datetime
import os

LOG_DIR = "housing_logs" # Directory name

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-M-S')}" # A current time tracking

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log" # We create a file for each log

# We make the log directory or folder
os.makedirs(LOG_DIR, exist_ok=True)

# Next, we create a filepath.......
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)