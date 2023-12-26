from sqlalchemy import String,Column,ForeignKey,Integer,desc,MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from connect import session,Session
from models import Reception
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

reception=[
    Reception(1,'nathan','nathan@gmail.com',6131)
]        
session.add_all(reception)
session.commit()
