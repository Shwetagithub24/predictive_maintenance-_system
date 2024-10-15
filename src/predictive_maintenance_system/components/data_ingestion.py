# 1. Fetch Data from MySQL 
# 2. Read in local
# 3. Train Test Split

import os
import sys
from src.predictive_maintenance_system.logger import logging
from src.predictive_maintenance_system.exception import CustomException
import pandas as pd

from dataclasses import dataclass   
from src.predictive_maintenance_system.utils import read_sql_data
from sklearn.model_selection import train_test_split

#to initialise input parameters
@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  #initialises raw_data_path, train_data_path and test_data_path

    def initiate_data_ingestion(self):
        try:
            # 1. Read data from MySQL
            df = read_sql_data()
            logging.info("Completed reading from MySQL Database.")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            # 2. Save Dataframe to raw_data.csv
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # 3. Train Test Split
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Train and Test data saved in .csv file")
            logging.info("Data Ingestion completed.")

            return (
               self.ingestion_config.train_data_path,
               self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)

