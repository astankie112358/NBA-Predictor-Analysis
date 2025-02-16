from sqlalchemy import Column, Integer, text, MetaData, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.orm import registry, mapper
import os

metadata = MetaData()
metadata = MetaData(schema='stg')

players_stats = Table(
    'stg_Boxscores', metadata,
    Column('Unnamed: 0', VARCHAR(3)),
    Column('Unnamed: 1', Integer),
    Column('PLAYER', VARCHAR(60)),
    Column('MP', VARCHAR(20)),
    Column('FG', VARCHAR(20)),
    Column('FGA', VARCHAR(20)),
    Column('FG%', VARCHAR(20)),
    Column('3P', VARCHAR(20)),
    Column('3PA', VARCHAR(20)),
    Column('3P%', VARCHAR(20)),
    Column('FT', VARCHAR(20)),
    Column('FTA', VARCHAR(20)),
    Column('FT%', VARCHAR(20)),
    Column('ORB', VARCHAR(20)),
    Column('DRB', VARCHAR(20)),
    Column('TRB', VARCHAR(20)),
    Column('AST', VARCHAR(20)),
    Column('STL', VARCHAR(20)),
    Column('BLK', VARCHAR(20)),
    Column('TOV', VARCHAR(20)),
    Column('PF', VARCHAR(20)),
    Column('PTS', VARCHAR(20)),
    Column('GmSc', VARCHAR(20)),
    Column('+/-', VARCHAR(20)),
    Column('TS%', VARCHAR(20)),
    Column('eFG%', VARCHAR(20)),
    Column('3PAr', VARCHAR(20)),
    Column('FTr', VARCHAR(20)),
    Column('ORB%', VARCHAR(20)),
    Column('DRB%', VARCHAR(20)),
    Column('TRB%', VARCHAR(20)),
    Column('AST%', VARCHAR(20)),
    Column('STL%', VARCHAR(20)),
    Column('BLK%', VARCHAR(20)),
    Column('TOV%', VARCHAR(20)),
    Column('USG%', VARCHAR(20)),
    Column('ORtg', VARCHAR(20)),
    Column('DRtg', VARCHAR(20)),
    Column('BPM', VARCHAR(20)),
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