# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'tasks_base'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'newp55!'


db_params = {'db_name': DATABASE_NAME, 'db_user': DATABASE_USER, 'db_password': DATABASE_PASSWORD}

engine=create_engine("postgresql://{db_user}:{db_password}@localhost/{db_name}".format(**db_params), echo=True)
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)

if __name__ == "__main__":

    print(engine)
    print(Base)
    print(SessionLocal)