from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from functools import wraps

engine = create_engine(
    "sqlite:///calendar.db",
    echo=True,
)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...

def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)


def db_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Session() as session:
            return func(session, *args, **kwargs)
        return wrapper