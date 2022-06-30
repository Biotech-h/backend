from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text

from backend.database.db import Base


class Company(Base):
    __tablename__ = 'companies'

    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=False)


class Job(Base):
    __tablename__ = 'jobs'

    uid = Column(Integer, primary_key=True)
    company_uid = Column(Integer, ForeignKey(Company.uid), nullable=False)
    name = Column(String, nullable=False)
    salary = Column(Integer, nullable=True)
    description = Column(Text, nullable=False)
    date_published = Column(Date, nullable=False)
    date_expiring = Column(Date, nullable=False)
    url = Column(String, nullable=False)
