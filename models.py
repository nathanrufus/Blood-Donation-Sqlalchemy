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


class BloodBank(Base):
    __tablename__ = "BloodBank"
    B_group = Column(String(100), primary_key=True)
    Total_packets =  Column(Integer(),nullable=True)

    def __init__(self,B_group,Total_packets):
        self.B_group =B_group
        self.Total_packets =Total_packets


class Blood(Base):
    __tablename__ = "Blood"
    B_code = Column(Integer(), primary_key=True,autoincrement=True)
    D_id =  Column(Integer(),ForeignKey('Donor.D_id'),nullable=True)
    B_group = Column(String(100),ForeignKey('BloodBank.B_group'), nullable=False)
    Packets =  Column(Integer(),nullable=True)

    def __init__(self,B_code,D_id,B_group,Packets):
        self.B_code =B_code
        self.D_id =D_id
        self.emaiB_groupl = B_group
        self.Packets =Packets
       
class Contact(Base):
    __tablename__ = "Contact"
    Contact_id = Column(Integer(), primary_key=True,autoincrement=True)
    B_group = Column(String(100),ForeignKey('BloodBank.B_group'), nullable=False)
    F_name = Column(String(100), nullable=False)
    C_packets =  Column(Integer(),nullable=True)
    Adress = Column(String(250), nullable=False)


    def __init__(self,Contact_id,B_group,F_name,C_packets,Adress):
        self.Contact_id =Contact_id
        self.B_group =B_group
        self.F_name = F_name
        self.C_packets =C_packets
        self.Adress =Adress

        
class Notification(Base):
    __tablename__ = "Notification"
    N_id = Column(Integer(), primary_key=True,autoincrement=True)
    NB_group = Column(String(100), nullable=False)
    NF_name = Column(String(100), nullable=False)
    N_packets =  Column(Integer(),nullable=True)
    N_Adress = Column(String(250), nullable=False)


    def __init__(self,N_id,NB_group,NF_name,N_packets,N_Adress):
        self.N_id =N_id
        self.NB_group =NB_group
        self.NF_name = NF_name
        self.N_packets =N_packets
        self.N_Adress =N_Adress
               