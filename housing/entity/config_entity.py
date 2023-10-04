# The Entity Configuration For My Machine Learning Pipeline/Development Cycle From Model Ingestion To Model Deployment
from collections import namedtuple

""" 
We create an instance of 'namedtuple' class to specify where to:
download dataset(URL),
create the folder for dataset (a zip folder),
create the folder to extract the dataset from (an extracted folder),
create the folder for ingested training dataset to,
create the folder for ingested test dataset to
"""
# For Data Ingestion
Data_Ingestion_Config = namedtuple(
    "DataIngestionConfig", 
    ["dataset_download_url", 'tgz_download_dir', 'raw_data_dir', 'ingested_train_dir','ingested_test_dir']
    )


# For Data Validation
Data_Validation_Config = namedtuple("DataValidationConfig", ["schema_file_path"]) #data_validation_configuration and the schema file path
#taking the columns names, the datatypes of columns


# For Data Transformation
Data_Transformation_Config = namedtuple(
    "DataTransformationConfig", 
    ["add_bedroom_per_room",
    "transformed_train_dir",
    "transform_test_dir",
    "preprocessed_object_file_path"
    ]
)


# For Model Training
Model_Trainer_Config = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy"])

# For Model Evaluation

Model_Evaluation_Config = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path", "time_stamp"])

# For Model Deployment

Model_Pusher_Config = namedtuple("ModelPusherConfig", ["export_dir_path"])

#Training Pipeline

Training_Pipeline_Config = namedtuple("TrainngPipelineConfig", ['artifacts_dir'])
