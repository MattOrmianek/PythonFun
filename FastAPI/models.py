from __future__ import annotations
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
