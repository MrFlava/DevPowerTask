from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from conf import  DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()