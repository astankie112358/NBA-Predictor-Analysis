import pandas
import pandas as pd
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

class DatabaseLoader:
    def __init__(self):
        db_username = 'nba_admin'
        db_password = os.getenv('NBA_ADMIN_PASS')
        db_host = 'localhost'
        db_port = '5432'
        db_name = 'NBA_Analysis'
        self.engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
    def get_files_to_load(self,path):
        with self.engine.connect() as connection:
            files = os.listdir(path)
            for file_name in files:
                file=pandas.read_csv(path+'\\'+file_name,low_memory=False)
                transaction = connection.begin()
                if 'Unnamed: 16_level_1' in file.columns:
                    file.drop(columns=['Unnamed: 16_level_1'], inplace=True)
                try:
                    file.to_sql('stg_Boxscores', connection, if_exists='append', index=False, schema='stg',index_label='id')
                    transaction.commit()
                except Exception as e:
                    transaction.rollback()
                    print(e)

databaseLoader = DatabaseLoader()
databaseLoader.get_files_to_load('D:\\Users\\Adam\\PycharmProjects\\NBA_GAMES\\2022')

