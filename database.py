# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_NAME = 'tasks_base'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'newp55!'
DATABASE_HOST = 'localhost'
#DATABASE_PORT = '5432'


db_params = {
    'db_name': DATABASE_NAME,
    'db_user': DATABASE_USER,
    'db_password': DATABASE_PASSWORD,
    'db_host': DATABASE_HOST
    #'db_port': DATABASE_PORT,
}


engine = create_engine("postgresql://{db_user}:{db_password}@{db_host}/{db_name}".format(**db_params), echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


if __name__ == "__main__":

    print(engine, Base, SessionLocal, sep='\n')