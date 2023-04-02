from sqlalchemy import Column, BigInteger, Text, ForeignKey, DateTime, func

from app.database.base_class import Base


class UserFeedback(Base):
    """Table to store user feedback."""

    __tablename__ = "user_feedback"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("bot_user.id"), nullable=False)
    feedback = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
