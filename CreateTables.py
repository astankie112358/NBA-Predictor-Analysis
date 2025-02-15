from sqlalchemy import Column, Integer, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy import create_engine
import os

Base = declarative_base()

class PlayersStats(Base):
    __tablename__ = 'stg_Boxscores'
    __table_args__ = {'schema': 'stg'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    season = Column(VARCHAR(6))
    unnamed_0 = Column('Unnamed: 0', VARCHAR(3))
    unnamed_1 = Column('Unnamed: 1', Integer)
    player = Column('PLAYER', VARCHAR(60))
    mp = Column('MP', VARCHAR(12))
    fg = Column('FG', VARCHAR(12))
    fga = Column('FGA', VARCHAR(12))
    fg_percent = Column('FG%', VARCHAR(12))
    three_p = Column('3P', VARCHAR(12))
    three_pa = Column('3PA', VARCHAR(12))
    three_p_percent = Column('3P%', VARCHAR(12))
    ft = Column('FT', VARCHAR(12))
    fta = Column('FTA', VARCHAR(12))
    ft_percent = Column('FT%', VARCHAR(12))
    orb = Column('ORB', VARCHAR(12))
    drb = Column('DRB', VARCHAR(12))
    trb = Column('TRB', VARCHAR(12))
    ast = Column('AST', VARCHAR(12))
    stl = Column('STL', VARCHAR(12))
    blk = Column('BLK', VARCHAR(12))
    tov = Column('TOV', VARCHAR(12))
    pf = Column('PF', VARCHAR(12))
    pts = Column('PTS', VARCHAR(12))
    gmsc = Column('GmSc', VARCHAR(12))
    plus_minus = Column('+/-', VARCHAR(12))
    ts_percent = Column('TS%', VARCHAR(12))
    efg_percent = Column('eFG%', VARCHAR(12))
    threepar = Column('3PAr', VARCHAR(12))
    ftr = Column('FTr', VARCHAR(12))
    orb_percent = Column('ORB%', VARCHAR(12))
    drb_percent = Column('DRB%', VARCHAR(12))
    trb_percent = Column('TRB%', VARCHAR(12))
    ast_percent = Column('AST%', VARCHAR(12))
    stl_percent = Column('STL%', VARCHAR(12))
    blk_percent = Column('BLK%', VARCHAR(12))
    tov_percent = Column('TOV%', VARCHAR(12))
    usg_percent = Column('USG%', VARCHAR(12))
    ortg = Column('ORtg', VARCHAR(12))
    drtg = Column('DRtg', VARCHAR(12))
    bpm = Column('BPM', VARCHAR(12))
    game_id = Column('GAME_ID', VARCHAR(14))


db_username = 'nba_admin'
db_password = os.getenv('NBA_ADMIN_PASS')
db_host = 'localhost'
db_port = '5432'
db_name = 'NBA_Analysis'

engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
with engine.connect() as connection:
    connection.execute(text("CREATE SCHEMA IF NOT EXISTS stg"))
    connection.commit()

Base.metadata.create_all(engine)