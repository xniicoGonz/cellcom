from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:12345@localhost:5433/postgres"

db = create_engine(db_string)
base = declarative_base()


class User(base):
    __tablename__ = 'user'
    email = Column(String, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    identificationCard = Column(String)
    phone = Column(String)
    address = Column(String)
    password = Column(String)
    rol = Column(String)

class Lines(base):
    __tablename__ = 'lines'
    numberline=Column(String, primary_key=True)
    customerIdentification=Column(String)
    state=Column(String)
    trademark=Column(String)

class Bill(base):
    __tablename__ = 'bills'
    value= Column(Integer)
    id_bill = Column(Integer, primary_key=True, autoincrement='ignore_fk')
    collectionDay=Column(Date)
    customerIdentification=Column(String)
    numberLine=Column(String)

class Customer(base):
    __tablename__= 'customer'
    namne=Column(String)
    lastname=Column(String)
    customerIdentification=Column(String, primary_key=True,)
    line=Column(String)
    dateBorn=Column(Date)

class equipment(base):
    __tablename__= 'equipment'
    lineNumber=Column(String)
    serial=Column(String)
    imei=Column(String, primary_key=True)
    trademark=Column(String)
    state= Column(String)

    

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)
