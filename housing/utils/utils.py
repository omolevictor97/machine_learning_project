import yaml
import sys
import os
from housing.logger import logging
from housing.exception import HousingException


def read_yaml_file(file_path:str) -> dict:
    """
    Reads a yaml file and returns an equivalent dictionary datatype
    """
    try:
        with open(file_path) as yaml_file:
            config_dict = yaml.safe_load(yaml_file)
            logging.info(f"Config Dictionary: {config_dict}")
            return config_dict
    except Exception as e:
        raise HousingException(e, sys) from e
