import functools
import logging
from typing import Any

from psycopg2.errors import UniqueViolation, StringDataRightTruncation  # noqa
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import scoped_session

from app.database.session import SessionLocal

logger = logging.getLogger(__name__)


def get_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = scoped_session(SessionLocal)()
        try:
            logger.info(
                "Database session opened, Session ObjectID %s", str(id(session))
            )
            func(*args, **kwargs, session=session)
        except Exception as e:
            logger.exception(e)
        finally:
            session.close()
            logger.info(
                "Database session closed, Session ObjectID %s", str(id(session))
            )

    return wrapper


class BaseController:
    __base_model__ = None
    __support_model__ = None
    __sub_model__ = None

    def __new__(cls, *args, **kwargs):
        cls._connection = kwargs["connection"]
        return super().__new__(cls)

    def __init__(self, connection):
        self._connection = connection

    @staticmethod
    def prepare_string(string: str):
        return string.strip().casefold()

    @classmethod
    def one_by_id(cls, id_: Any):
        return (
            cls._connection.query(cls.__base_model__)
            .filter(cls.__base_model__.id == id_)
            .first()
        )

    @classmethod
    def all(cls, offset: int = 0, limit: int = 100):
        return (
            cls._connection.query(cls.__base_model__).offset(offset).limit(limit).all()
        )

    @classmethod
    def all_by_support_model(cls, offset: int = 0, limit: int = 100):
        return (
            cls._connection.query(cls.__support_model__)
            .offset(offset)
            .limit(limit)
            .all()
        )

    @classmethod
    def _generic_create(cls, model, *args, **kwargs):
        base_model = model(*args, **kwargs)
        try:
            cls._connection.add(base_model)
            cls._connection.commit()
            cls._connection.refresh(base_model)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
            cls._connection.rollback()
        except DataError as e:
            assert isinstance(e.orig, StringDataRightTruncation)
            cls._connection.rollback()
        return base_model

    @classmethod
    def create(cls, *args, **kwargs):
        return cls._generic_create(cls.__base_model__, *args, **kwargs)

    @classmethod
    def create_by_support_model(cls, *args, **kwargs):
        return cls._generic_create(cls.__support_model__, *args, **kwargs)

    @classmethod
    def create_by_sub_model(cls, *args, **kwargs):
        return cls._generic_create(cls.__sub_model__, *args, **kwargs)

    @classmethod
    def _generic_remove(cls, model, id_: int):
        base_model = cls._connection.query(model).get(id_)
        cls._connection.delete(base_model)
        try:
            cls._connection.commit()
            return True
        except Exception as e:
            logger.error(e)
            cls._connection.rollback()
            return False

    @classmethod
    def remove(cls, id_: int):
        return cls._generic_remove(cls.__base_model__, id_=id_)

    @classmethod
    def remove_by_support_model(cls, id_: int):
        return cls._generic_remove(cls.__support_model__, id_=id_)

    @classmethod
    def remove_by_sub_model(cls, id_: int):
        return cls._generic_remove(cls.__sub_model__, id_=id_)

    @classmethod
    def update(cls, id_: int, **kwargs):
        return cls._generic_update(cls.__base_model__, id_=id_, **kwargs)

    @classmethod
    def _generic_update(cls, model, id_: int, **kwargs):
        cls._connection.query(model).filter(cls.__base_model__.id == id_).update(
            **kwargs
        )
        try:
            cls._connection.commit()
            return True
        except Exception as e:
            logger.error(e)
            cls._connection.rollback()
            return False
