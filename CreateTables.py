from sqlalchemy import Column, Integer, text, MetaData, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.orm import registry, mapper
import os

metadata = MetaData()
metadata = MetaData(schema='stg')

# Define the table using the metadata object
players_stats = Table(
    'stg_Boxscores', metadata,
    Column('Unnamed: 0', VARCHAR(3)),
    Column('Unnamed: 1', Integer),
    Column('PLAYER', VARCHAR(60)),
    Column('MP', VARCHAR(13)),
    Column('FG', VARCHAR(13)),
    Column('FGA', VARCHAR(13)),
    Column('FG%', VARCHAR(13)),
    Column('3P', VARCHAR(13)),
    Column('3PA', VARCHAR(13)),
    Column('3P%', VARCHAR(13)),
    Column('FT', VARCHAR(13)),
    Column('FTA', VARCHAR(13)),
    Column('FT%', VARCHAR(13)),
    Column('ORB', VARCHAR(13)),
    Column('DRB', VARCHAR(13)),
    Column('TRB', VARCHAR(13)),
    Column('AST', VARCHAR(13)),
    Column('STL', VARCHAR(13)),
    Column('BLK', VARCHAR(13)),
    Column('TOV', VARCHAR(13)),
    Column('PF', VARCHAR(13)),
    Column('PTS', VARCHAR(13)),
    Column('GmSc', VARCHAR(13)),
    Column('+/-', VARCHAR(13)),
    Column('TS%', VARCHAR(13)),
    Column('eFG%', VARCHAR(13)),
    Column('3PAr', VARCHAR(13)),
    Column('FTr', VARCHAR(13)),
    Column('ORB%', VARCHAR(13)),
    Column('DRB%', VARCHAR(13)),
    Column('TRB%', VARCHAR(13)),
    Column('AST%', VARCHAR(13)),
    Column('STL%', VARCHAR(13)),
    Column('BLK%', VARCHAR(13)),
    Column('TOV%', VARCHAR(13)),
    Column('USG%', VARCHAR(13)),
    Column('ORtg', VARCHAR(13)),
    Column('DRtg', VARCHAR(13)),
    Column('BPM', VARCHAR(13)),
    Column('GAME_ID', VARCHAR(14))
)

db_username = 'nba_admin'
db_password = os.getenv('NBA_ADMIN_PASS')
db_host = 'localhost'
db_port = '5432'
db_name = 'NBA_Analysis'

engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
with engine.connect() as connection:
    connection.execute(text("CREATE SCHEMA IF NOT EXISTS stg"))
    connection.commit()

metadata.create_all(engine)