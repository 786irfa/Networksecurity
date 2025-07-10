from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.entity.config_entity import DataIngestionConfig
from Networksecurity.entity.config_entity import TrainingPipeLineConfig
import logging
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipeLineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("enter the try block")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        ##a = 1 / 0
        ##print("this will be not printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)