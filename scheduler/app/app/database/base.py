# Import all the models, so that Base has them before being
# imported by Alembic
from app.database.base_class import Base  # noqa
from app.models.users import BotUser  # noqa
from app.models.users import UserState  # noqa
from app.models.users import UserMood  # noqa
from app.models.feedback import UserFeedback  # noqa
from app.models.activity import Activity  # noqa
from app.models.mood import Mood  # noqa
from app.models.mood import Spectrum  # noqa
