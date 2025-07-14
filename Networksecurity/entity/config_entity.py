from datetime import datetime
import os
from Networksecurity.constants import training_pipeline

print(training_pipeline.pipeline_name)
print(training_pipeline.artifact_dir)


class TrainingPipeLineConfig:
    def __init__(self, timestamp=datetime.now()):
        self.pipeline_name = training_pipeline.pipeline_name
        self.artifact_dir = training_pipeline.artifact_dir
        self.schema_file_path = os.path.join("data_schema", "schema.yaml")  # ✅ FIXED: added self.
        self.timestamp: str = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipeLineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.data_ingestion_dir_name
        )

        self.data_ingestion_feature_store: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_feature_store_dir,
            training_pipeline.data_ingestion_file_name
        )

        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_ingested_dir,
            training_pipeline.train_file_name
        )

        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_ingested_dir,
            training_pipeline.test_file_name
        )

        self.train_test_split: float = training_pipeline.data_ingestion_train_test_split_ratio
        self.collection_name: str = training_pipeline.data_ingestion_collection_name
        self.database_name: str = training_pipeline.data_ingestion_database_name


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipeLineConfig):
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.data_validation_dir_name
        )

        self.schema_file_path = training_pipeline_config.schema_file_path  # ✅ FIXED: stored as instance attribute

        self.data_validation_valid_dir: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.data_validation_valid_dir
        )

        self.data_validation_invalid_dir: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.data_validation_invalid_dir
        )

        self.valid_test_file_path: str = os.path.join(
            self.data_validation_valid_dir,
            training_pipeline.test_file_name
        )

        self.valid_train_file_path: str = os.path.join(
            self.data_validation_valid_dir,
            training_pipeline.train_file_name
        )

        self.invalid_train_file_path: str = os.path.join(
            self.data_validation_invalid_dir,
            training_pipeline.train_file_name
        )

        self.invalid_test_file_path: str = os.path.join(
            self.data_validation_invalid_dir,
            training_pipeline.test_file_name
        )

        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.data_validation_drift_dir,
            training_pipeline.data_validation_drift_report_file_name
        )
