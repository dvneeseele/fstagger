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


class FileTag(Base):
    __tablename__ = 'file_tags'

    file_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, primary_key=True)
    meta_id = Column(Integer, primary_key=True)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)


# Metadata outside of basic file data
class TagMetadata(Base):
    __tablename__ = 'metadata'

    id = Column(Integer, primary_key=True)
    label_color = Column(String)
    note = Column(String)
    icon_path = Column(String)

Base.metadata.create_all(engine)