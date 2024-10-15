import os
import sys
from src.predictive_maintenance_system.exception import CustomException
from src.predictive_maintenance_system.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

#load database configuration
load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    
    logging.info("Reading SQL database started.")
    try:
        # 1. connect to MySQL
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connected to the Database: {mydb}")

        
        # 2. Read Data
        df = pd.read_sql_query('select * from engine_data',mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)
