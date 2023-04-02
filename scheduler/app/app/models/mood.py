from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    JSON,
    ForeignKey,
)

from app.database.base_class import Base


class Mood(Base):
    __tablename__ = "mood"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    callback = Column(String, unique=True)
    translations = Column(JSON, server_default="{}")
    weight = Column(Integer)


class Spectrum(Base):
    __tablename__ = "spectrum"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    mood_id = Column(BigInteger, ForeignKey("mood.id"), nullable=False)
    callback = Column(String, unique=True)
    translations = Column(JSON, server_default="{}")
    weight = Column(Integer)
