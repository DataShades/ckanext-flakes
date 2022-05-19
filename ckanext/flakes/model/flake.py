from __future__ import annotations

from collections import ChainMap
from datetime import datetime
from typing import Any

import ckan.model as model
from ckan.lib.dictization import table_dictize
from ckan.model.types import make_uuid
from sqlalchemy import Column, DateTime, ForeignKey, UnicodeText
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey

from .base import Base


class Flake(Base):
    __tablename__ = "flakes_flake"

    id = Column(UnicodeText, primary_key=True, default=make_uuid)
    data = Column(JSONB, nullable=False)
    modified_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    author_id = Column(UnicodeText, ForeignKey(model.User.id), nullable=False)
    parent_id = Column(UnicodeText, ForeignKey("flakes_flake.id"))

    author = relationship(
        model.User,
        backref=backref("flakes", cascade="all, delete-orphan"),
    )
    parent = relationship(
        "Flake",
        backref=backref(
            "flakes", cascade="all, delete-orphan", single_parent=True
        ),
        remote_side=[id],
    )

    def for_json(self, context: dict[str, Any]):
        result = table_dictize(self, context)

        if context.get("expand"):
            sources: list[dict[str, Any]] = [self.data]
            parent = self.parent

            while parent:
                sources.append(parent.data)
                parent = parent.parent

            result["data"] = dict(ChainMap(*sources))

        return result
