from app.controllers import BaseController
from app.models.categories import Activity
from app.models.users import UserCategory


class CategoryController(BaseController):
    __base_model__ = UserCategory
    __sub_model__ = Activity

    def __init__(self, connection):
        super().__init__(connection=connection)

    def insert(self, activity: str, user_id: int):
        activity_item = (
            self._connection.query(self.__sub_model__)
            .filter(self.__sub_model__.title == activity)
            .first()
        )
        return self.create(
            user_id=user_id,
            activity_id=activity_item.id,
        )
