from backend.database.models import *
from backend.database.db import Base, engine


if name == '__main__':
    Base.metadata.create_all(bind=engine)
