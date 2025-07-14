from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_validation import DataValidation
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logg.logger import logging
from Networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    TrainingPipeLineConfig
)
import sys

if __name__ == "__main__":
    try:
        # Step 1: Initialize pipeline config
        training_pipeline_config = TrainingPipeLineConfig()

        # Step 2: Data Ingestion
        logging.info("Initializing data ingestion config...")
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        logging.info("Starting data ingestion...")
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully.")
        print("Data Ingestion Artifact:")
        print(data_ingestion_artifact)

        # Step 3: Data Validation
        logging.info("Initializing data validation config...")
        data_validation_config = DataValidationConfig(training_pipeline_config)

        logging.info("Starting data validation...")
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed successfully.")
        print("Data Validation Artifact:")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
