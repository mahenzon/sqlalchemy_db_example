from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)
