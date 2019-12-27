from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username}>"
