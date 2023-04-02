from sqlalchemy import (
    Column,
    String,
    BigInteger, ForeignKey,
)

from app.database.base_class import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(String, unique=True)


class Activity(Base):
    __tablename__ = "activity"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(String, unique=True)
    category = Column(BigInteger, ForeignKey("category.id"), nullable=False)
    social_media_estimation = Column(String, nullable=False)
    scientific_estimation = Column(String, nullable=False)
    scientific_source = Column(String, nullable=False)
