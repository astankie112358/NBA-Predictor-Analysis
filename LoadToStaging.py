import pandas
import pandas as pd
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

class DatabaseLoader:
    def __init__(self):
        db_username = 'Admin'
        db_password = os.getenv('NBA_ADMIN_PASS')
        db_host = 'localhost'
        db_port = '5432'
        db_name = 'NBA_Analysis'
        #self.engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
    def get_files_to_load(self,path):
        files = os.listdir(path)
        for file_name in files:
            file=pandas.read_csv(path+'\\'+file_name,low_memory=False)
            for column in file.columns:
                if pd.api.types.is_string_dtype(file[column]):
                    print(column," varchar ",file[column].str.len().max())
                else:
                    print(column, "int")


databaseLoader = DatabaseLoader()
databaseLoader.get_files_to_load('D:\\Users\\Adam\\PycharmProjects\\NBA_GAMES\\2023')

