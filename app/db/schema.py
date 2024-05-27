from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime, timezone

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    is_published = Column(Boolean, default=False)

    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    category = relationship('Category', back_populates='post')
    tags = relationship('Tag', back_populates='post')


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    post = relationship('Post', back_populates='comments')
    user = relationship('User', back_populates='comments')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('Post', back_populates='category')


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('Post', back_populates='tags')


class connect():

    try:
        engine = create_engine('postgresql://postgres:admin@localhost/blog')
        print("Database is connected sucessfully!")
    except Exception as ex:
        print("Unable to connect to the database. Reason: %s" % ex)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    users = [
        User(username='user1', email='user1@example.com', password='password1'),
        User(username='user2', email='user2@example.com', password='password2'),
        User(username='user3', email='user3@example.com', password='password3'),
        User(username='user4', email='user4@example.com', password='password4'),
        User(username='user5', email='user5@example.com', password='password5'),
    ]

    categories = [
        Category(name='Technology', post_id=1),
        Category(name='Health', post_id=2),
        Category(name='Travel', post_id=3),
        Category(name='Food', post_id=4),
        Category(name='Other', post_id=5),
    ]

    posts = [
        Post(title='Post 1', content='Content for post 1', user_id=1),
        Post(title='Post 2', content='Content for post 2', user_id=2),
        Post(title='Post 3', content='Content for post 3', user_id=3),
        Post(title='Post 4', content='Content for post 4', user_id=4),
        Post(title='Post 5', content='Content for post 5', user_id=5),
    ]

    comments = [
        Comment(content='Comment 1 on post 1', post_id=1, user_id=1),
        Comment(content='Comment 2 on post 2', post_id=2, user_id=2),
        Comment(content='Comment 3 on post 3', post_id=3, user_id=3),
        Comment(content='Comment 4 on post 4', post_id=4, user_id=4),
        Comment(content='Comment 5 on post 5', post_id=5, user_id=5),
    ]

    tags = [
        Tag(name='Tag1', post_id=1),
        Tag(name='Tag2', post_id=2),
        Tag(name='Tag3', post_id=3),
        Tag(name='Tag4', post_id=4),
        Tag(name='Tag5', post_id=5),
    ]

    # add dummy response to the table
    session.add_all(users)
    session.commit()
    session.add_all(posts)
    session.commit()
    session.add_all(categories)
    session.commit()
    session.add_all(comments)
    session.commit()
    session.add_all(tags)
    session.commit()
