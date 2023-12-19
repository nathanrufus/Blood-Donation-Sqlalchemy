from sqlalchemy import String,Column,ForeignKey,Integer,desc,MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from connect import session,Session


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base =declarative_base(metadata=metadata)

class Reception(Base):
    __tablename__ = "Reception"
    E_id = Column(Integer(), primary_key=True,autoincrement=True)
    name =  Column(String(100),nullable=True)
    email = Column(String(100), nullable=False)
    password =  Column(Integer(),nullable=True)

    def __init__(self,E_id,name,email,password):
        self.E_id =E_id
        self.name =name
        self.email = email
        self.password =password

class Donor(Base):
    __tablename__ = "Donor"
    D_id = Column(Integer(), primary_key=True,autoincrement=True)
    Dname =  Column(String(100),nullable=True)
    Sex =  Column(String(10),nullable=True)
    Age =  Column(String(10),nullable=True)
    Weight =  Column(Integer(),nullable=True)
    Address =  Column(String(100),nullable=True)
    Disease =  Column(String(100),nullable=True)
    Demail = Column(String(100), nullable=False)

    def __init__(self,D_id,Dname,Sex,Age,Weight,Address,Disease,Demail,):
        self.D_id =D_id
        self.Dname =Dname
        self.Sex =Sex
        self.Age =Age
        self.Weight =Weight
        self.Address =Address
        self.Disease =Disease
        self.Demail = Demail