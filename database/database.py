from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://gelypfxhemiufu:eae001554f47a9af6172e2485c8551df51b9df32ec2d9a23fc956ee4cd538a31@ec2-52-87-107-83.compute-1.amazonaws.com:5432/devup0av636ugh"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
