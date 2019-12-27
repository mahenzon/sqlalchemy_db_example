from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base
from .user import User


class Post(Base):

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    title = Column(String(32), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, nullable=False, default=False)
    user = relationship("User", back_populates="posts", lazy="joined")

    def __repr__(self):
        return f"<Post #{self.id} {self.title}>"
