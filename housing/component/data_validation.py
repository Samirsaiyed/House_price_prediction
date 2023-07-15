
from housing.logger import logging
from housing.exception import HousingException
import os,sys
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import pandas as pd





class DataValidation:
    
    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
           self.data_validation_config = data_validation_config
           self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_train_and_test_df(self):
        train_df = pd.read(self.data_ingestion_artifact.train_file_path)
        test_df = pd.read(self.data_ingestion_artifact.test_file_path)
        return train_df,test_df

    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info("Checking if training and testing file is avilable")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available =  is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists? -> {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                
                message = f"Training file: {training_file} or testing file: {testing_file} is not present"

                raise Exception(message)
            
            
            return is_available

        except Exception as e:
            raise HousingException(e,sys) from e

    
    def validate_dataset_schema(self)-> bool:
        try:
            validation_status = False
            
            
            validation_status = True
            return validation_status

        except Exception as e:
            raise HousingException(e,sys) from e


    def save_data_drift_report(self):

        try:  
            pass
            '''
            report = Report(metrics=[DataDriftPreset(), ])
            train_df,test_df = self.get_train_and_test_df()
            report.run(train_df,test_df)
            report = json.loads(report.json())
            with open(self.data_validation_config.report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)
            return report
            '''
            
        except Exception as e:
            raise HousingException(e,sys) from e 


    def save_data_drift_report_page(self):
        try:
            pass
            '''
            report = Report(metrics=[
            ColumnSummaryMetric(column_name='AveRooms'),
            ColumnQuantileMetric(column_name='AveRooms', quantile=0.25),
            ColumnDriftMetric(column_name='AveRooms')
            ])

            train_df,test_df = self.get_train_and_test_df()

            report.run(train_df,test_df)

            report.save(self.data_validation_config.report_page_file_path)
            '''    
        except Exception as e:
            raise HousingException(e,sys) from E

    def is_data_drift_found(self)-> bool:
        try:
            pass
            '''
            report = self.save_data_drift_report()
            self.save_data_drift_report_page()
            
            return True
            '''
        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_validation(self)-> DataValidationArtifact:
        try:

            self.is_train_test_file_exists()

            self.validate_dataset_schema()

            self.is_data_drift_found()

            data_validatiob_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated= True,
                message= "Data validation perform successfully."
                
            )
            logging.info(f"Data validation artifact: {data_validatiob_artifact}")

        except Exception as e:
            raise HousingException(e,sys) from e