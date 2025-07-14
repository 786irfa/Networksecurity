from Networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from Networksecurity.entity.config_entity import DataValidationConfig
from Networksecurity.logg.logger import logging
from Networksecurity.exception.exception import NetworkSecurityException

from scipy.stats import ks_2samp
import pandas as pd
import numpy as np
import os
import sys
from Networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

            self.schema_file_path = self.data_validation_config.schema_file_path
            self._schema_config = read_yaml_file(self.schema_file_path)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            required_columns = self._schema_config["columns"]
            expected_col_count = len(required_columns)

            logging.info(f"Expected number of columns: {expected_col_count}")
            logging.info(f"DataFrame columns: {len(dataframe.columns)}")

            return len(dataframe.columns) == expected_col_count

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_number_of_numerical_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            numerical_columns = dataframe.select_dtypes(include=[np.number]).columns.tolist()
            logging.info(f"Numerical columns found: {numerical_columns}")

            return len(numerical_columns) > 0

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}

            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                test_result = ks_2samp(d1, d2)

                drift_detected = test_result.pvalue < threshold
                if drift_detected:
                    status = False

                report[column] = {
                    "p_value": float(test_result.pvalue),
                    "drift_status": drift_detected
                }

            drift_report_file_path = self.data_validation_config.drift_report_file_path
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)

            return status

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            # Read training and test data
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_df = self.read_data(train_file_path)
            test_df = self.read_data(test_file_path)

            error_message = ""

            # Validate number of columns
            if not self.validate_number_of_columns(train_df):
                error_message += "Training data column count mismatch. "

            if not self.validate_number_of_columns(test_df):
                error_message += "Test data column count mismatch. "

            # Validate numerical columns
            if not self.validate_number_of_numerical_columns(train_df):
                error_message += "Training data lacks numerical columns. "

            if error_message:
                raise NetworkSecurityException(error_message, sys)

            # Detect dataset drift
            drift_status = self.detect_dataset_drift(base_df=train_df, current_df=test_df)

            # Save validated files
            os.makedirs(os.path.dirname(self.data_validation_config.valid_train_file_path), exist_ok=True)
            train_df.to_csv(self.data_validation_config.valid_train_file_path, index=False)
            test_df.to_csv(self.data_validation_config.valid_test_file_path, index=False)

            # Prepare artifact
            validation_artifact = DataValidationArtifact(
                validation_status=drift_status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )

            return validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
