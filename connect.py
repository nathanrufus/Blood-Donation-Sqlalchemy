from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db='mysql+mysqlconnector://root:6131a21A?@localhost/Blood_Donation_management'
engine=create_engine(db)
Session =sessionmaker(bind=engine)
session = Session()