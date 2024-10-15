from src.predictive_maintenance_system.logger import logging
from src.predictive_maintenance_system.exception import CustomException
import sys
from src.predictive_maintenance_system.components.data_ingestion import DataIngestion


if __name__=="__main__":
    logging.info("The execution has started.")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
         raise CustomException(e,sys)