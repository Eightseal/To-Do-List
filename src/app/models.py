from datetime import datetime, timedelta, timezone

from flask import render_template
from flask_dance.consumer.storage.sqla import (
    OAuthConsumerMixin,
)
from flask_login import UserMixin
from sqlalchemy import ForeignKey, LargeBinary, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str | None] = mapped_column(nullable=True)
    email: Mapped[str | None] = mapped_column(nullable=True)
    active: Mapped[bool | None] = mapped_column(nullable=True, default=True)

    def __init__(
        self, username: str | None = None, email: str | None = None, active: bool | None = True
    ):
        self.username = username
        self.email = email
        self.active = active


class To_Do_List(db.Model):
    __tablename__ = "to_do_list"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str | None] = mapped_column(nullable=False)
    to_do: Mapped[str | None] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=True, default=datetime.now(timezone.utc))

    def __init__(self, task_name: str, to_do: str, timestamp: datetime):
        self.task_name = task_name
        self.to_do = to_do
        self.timestamp = timestamp

    @property
    def formated_timestamp(self):
        timestamp = self.timestamp + timedelta(hours=2)

        return timestamp.strftime("%Y-%m-%d %H:%M:%S")
