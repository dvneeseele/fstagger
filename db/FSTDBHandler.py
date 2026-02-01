from FSTModels import File, engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import select

class FSTDBHandler():
    def __init__(self):
        
        Session = sessionmaker(bind=engine)
        self.session = Session()

    # Just using name, hash, and size for testing
    def createFileRecord(self, dir, name, hash, size):
        user_file = File(directory=dir,
            filename=name,
            file_hash=hash,
            size=size
        )
        
        self.session.add(user_file)
        self.session.commit()

    def getAllRecords(self, table):
        # just fetch the file's directory and name for now.
        all_records_query = self.session.query(table.directory + '/' + table.filename)
        
        print("Total Records:", all_records_query.count())

        return all_records_query
    
