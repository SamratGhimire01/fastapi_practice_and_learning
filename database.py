from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URl = "mysql+pymysql://samrat01:Samrat2003@localhost/school_db"
engin = create_engine(URl)
sessionmaker = sessionmaker(autocommit=False,autoflush=False,bind=engin)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()