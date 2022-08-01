import os

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship, sessionmaker

Base = declarative_base()

database_uri = os.environ.get("DATABASE_URI", "sqlite:///test.db")
engine = create_engine(database_uri, connect_args={"check_same_thread": False})


LocalSession = sessionmaker(bind=engine)
db: Session = LocalSession()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)
    addresses = relationship("Address", back_populates="user")

    def __str__(self):
        return f"User ({self.id})"


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)
    zipcode = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="addresses")

    def __str__(self):
        return f"Address ({self.id})"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    lorem = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="profile")

    def __str__(self):
        return f"Profile ({self.id})"
