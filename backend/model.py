from backend.db import Base


class Company(Base):
    id: Column(Integer, primary_key=True)
    name: Column(String, nullable=False)
    region: Column(String, nullable=False)
    category: Column(String, nullable=False)
    description: Column(Text, nullable=False)
