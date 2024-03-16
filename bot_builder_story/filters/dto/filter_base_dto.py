import uuid

from sqlmodel import SQLModel
from typing import Optional

from ..enum import FilterOperator


class FilterBaseDto(SQLModel):
    id: Optional[uuid.UUID] = None
    attribute: Optional[str] = None
    value: Optional[str] = None
    operator: Optional[FilterOperator] = None
    story_block_id: Optional[str] = None
    parent_id: Optional[uuid.UUID] = None
    sub_exprs: Optional[list["FilterBaseDto"]] = None
