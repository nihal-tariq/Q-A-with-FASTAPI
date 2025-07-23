from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


URl_DATABASE = 'postgresql://postgres:1234@localhost:1234/QuizApplication'

engine = create_engine(URl_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()