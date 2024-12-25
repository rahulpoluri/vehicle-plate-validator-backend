from sqlalchemy import TIMESTAMP, Column, Integer, String

from application.db.connection import Base


class Plates(Base):
    __tablename__ = "plates"
    id = Column(Integer, primary_key=True, nullable=False)
    plate = Column(String(20), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
