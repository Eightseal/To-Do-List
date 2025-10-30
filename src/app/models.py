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
