from backend.database.db import Base, engine
from backend.database.models import *  # noqa: F401, F403, WPS347

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
