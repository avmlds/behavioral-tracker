from app.controllers import BaseController
from app.models import UserFeedback


class FeedbackController(BaseController):
    __base_model__ = UserFeedback

    def __init__(self, connection):
        super().__init__(connection=connection)

    def insert(self, feedback: str, user_id: int):
        return self.create(
            user_id=user_id,
            feedback=feedback,
        )
