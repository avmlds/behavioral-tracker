from sqlalchemy import (
    Column,
    String,
    Boolean,
    Numeric,
    BigInteger,
    ForeignKey,
    CheckConstraint,
    DateTime,
    func,
    JSON,
)

from app.database.base_class import Base
from app.constants.states import ALL_STATES_STRING


class BotUser(Base):
    __tablename__ = "bot_user"

    id = Column(BigInteger, nullable=False, primary_key=True)
    balance = Column(Numeric(precision=18, scale=2), default=0, nullable=False)
    is_blocked = Column(Boolean, nullable=False, default=False)
    name = Column(String)
    login = Column(String)
    created_at = Column(DateTime, server_default=func.now())


class UserState(Base):
    __tablename__ = "user_state"
    __tableargs__ = (CheckConstraint(f"user_state in ({ALL_STATES_STRING})"),)

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("bot_user.id"), unique=True)
    user_state = Column(String, nullable=False)
    user_state_data = Column(JSON, server_default="{}")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())


class UserCategory(Base):
    __tablename__ = "user_category"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("bot_user.id"))
    activity_id = Column(BigInteger, ForeignKey("activity.id"))
    created_at = Column(DateTime, server_default=func.now())
