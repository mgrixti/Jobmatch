__author__ = 'Matthew Grixti'

from sqlalchemy import *
from sqlalchemy.orm import *

class DbConnection():

    # Establish connection to Database
    def connect(self):
        #Create db engine. Pass in connection string.
        engine = create_engine('mysql+mysqlconnector://jobmatch:Pennyworth2@mysql.mattgrixti.com/jobmatch', echo=True)
        Session = sessionmaker(bind=engine)
        return Session()

    def close(self, engine):
        engine.close()
