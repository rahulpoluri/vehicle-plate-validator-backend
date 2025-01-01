from sqlalchemy import TIMESTAMP, Column, Integer, String

from application.db.connection import Base, get_db
from application.db.crud.common import Mixin


class Basemodel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False)


Basemodel.db_session = get_db()


class Plates(Basemodel, Mixin):
    __tablename__ = "plates"
    plate = Column(String(20), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)

    class Config:
        orm_mode = True


class Users(Basemodel, Mixin):
    __tablename__ = "users"
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)

    class Config:
        orm_mode = True
