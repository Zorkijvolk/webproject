import sqlalchemy
from .db_session import SqlAlchemyBase


class HelpTable(SqlAlchemyBase):
    __tablename__ = 'help_table'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
