from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# server = 'server_name'
# database = 'database_name'
# username = 'username'
# password = 'password'

# SQLALCHEMY_DATABASE_URL = "postgresql://usuario:senha@host/nome_do_database"
# SQLALCHEMY_DATABASE_URL = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL
    "sqlite:///db_atas.db", echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
