from sqlalchemy.ext.declarative import declarative_base, declared_attr
from utils import camel_case_to_snake_case

from config import DB_TABLES_PREFIX
from .session import Session

class CustomBase:
    """
    Custom base for all project's models
    """

    # access session from models
    query = Session.query_property()

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return camel_case_to_snake_case(cls.__name__, prefix=DB_TABLES_PREFIX)


Base = declarative_base(cls=CustomBase)
