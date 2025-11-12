import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
from decouple import config

#config = configparser.ConfigParser()
#config.read('alembic.ini')

#SQLALCHEMY_DATABASE_URL = config.get('alembic', 'sqlalchemy.url')
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://vms_user:abc123!!@192.168.0.102:3306/vms_db'

# --- THIS IS THE CORRECTED LINE ---
SQLALCHEMY_DATABASE_URL = config('DATABASE_URL')
# --- END CORRECTION ---

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)

Base = declarative_base()

conn = engine.connect().execution_options(autocommit=True)