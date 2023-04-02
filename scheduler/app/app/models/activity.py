from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    JSON,
)

from app.database.base_class import Base


class Activity(Base):
    __tablename__ = "activity"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    callback = Column(String, unique=True)
    translations = Column(JSON, server_default="{}")
    weight = Column(Integer, unique=True)
