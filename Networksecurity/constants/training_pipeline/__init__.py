import os
import sys
import numpy as np
import pandas as pd
target_column="Result"
pipeline_name :str ="Networksecurity"
artifact_dir:str ="artifacts"
schema_file_path=os.path.join("data_schema","schema.yaml")
'''
data ingestion related constant staart with data ingestion variable name
'''

data_ingestion_collection_name: str = "networkdata"
data_ingestion_database_name: str = "IRFANAI"
data_ingestion_dir_name:str = "data_ingestion"
data_ingestion_feature_store_dir:str = "feature_store"
data_ingestion_ingested_dir:str ="ingested"
data_ingestion_train_test_split_ratio:float=0.2
ata_ingestion_raw_data_dir: str = "raw_data"
data_ingestion_processed_data_dir: str = "processed_data"
data_ingestion_file_name: str = "phising_dataset_predict.csv"
data_ingestion_mongo_uri_env_var: str = "MONGO_DB_URL"
train_file_name="training"
test_file_name="testing"


"""data validation related things start with data_validation_var name"""
data_validation_dir_name:str="data validation"
data_validation_valid_dir:str="validated"
data_validation_invalid_dir:str="invalid"
data_validation_drift_dir:str="drift_report"
data_validation_drift_report_file_name:str="report.yaml"
