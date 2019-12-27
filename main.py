# Можем просто импортировать модели, чтобы проинициализировать их всех
# # noinspection PyUnresolvedReferences
# import models

# не страшно, что Base импортируем раньше.
# Главное проинициализировать модели до использования metadata
from db.base_class import Base
from db.session import engine, Session
# либо хоть что-то импортируем, все модели проинициализируются
from models import User, Post


def create_tables():
    Base.metadata.create_all(engine)
    print("Created tables")


def create_rows():
    session = Session()

    user = User(username="demo")
    session.add(user)
    session.flush()

    post1 = Post(user_id=user.id, title="Flask lesson", text="ok, here we go again")
    post2 = Post(user_id=user.id, title="Django lesson", text="Demo again?")
    session.add(post1)
    session.add(post2)

    session.commit()
    print("Created entities")


# noinspection PyUnresolvedReferences
# нет свойства query у модели, по хорошему нужно сделать
# аннотацию на Base. Не уверен, как правильно это сделать
def fetch_some_data():
    user = User.query.filter_by(id=1).one()
    print("user:", user)
    print("his posts:", user.posts)

    post1 = Post.query.filter(Post.title == "Flask lesson").first()
    post2 = Post.query.filter_by(text="Demo again?").one()
    print("post1:", post1)
    print("post2:", post2)


if __name__ == "__main__":
    create_tables()
    create_rows()
    fetch_some_data()
