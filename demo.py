from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config=Configuartion().get_data_validation_config()
        #print(data_validation_config)
       
        #data_transfomation_config = Configuartion().#get_data_transformation_config()
        #print(data_transfomation_config)
        #schema_file_path=r"C:\Users\samir saiyed\Desktop\project\House_price_prediction\config\schema.yaml"
        #file_path = r"C:\Users\samir saiyed\Desktop\project\House_price_prediction\housing\artifact\data_ingestion\2023-07-15-15-43-57\ingested_data\train\housing.csv"

        #df=DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)




    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()
 
