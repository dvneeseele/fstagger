from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///database.db")

Base = declarative_base()

class File(Base):
    __tablename__ = 'files'

    # Just adding most columns that will be needed eventually
    id = Column(Integer, primary_key=True)
    directory = Column(String)
    filename = Column(String)
    file_hash = Column(String)
    creation_time = Column(String)
    modified_time = Column(String)
    size = Column(Integer)
    mime = Column(String)

    def __repr__(self):
        return f"ID={self.id}, DIR={self.directory}, NAME={self.filename}, hash={self.file_hash}"
