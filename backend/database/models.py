from sqlalchemy import Column, Integer, String, Text

from backend.database.db import Base


class Company(Base):
    __tablename__ = 'companies'

    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=False)
