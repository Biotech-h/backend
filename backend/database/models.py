from sqlalchemy import Column, Integer, String, Text, ForeignKey

from backend.database.db import Base


class Company(Base):
    __tablename__ = 'companies'

    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=False)


class Vacancy(Base):
    __tablename__ = 'vacancies'

    company_uid = Column(Integer, ForeignKey(Company.uid), nullable=False)
    vacancy_name = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=False)
