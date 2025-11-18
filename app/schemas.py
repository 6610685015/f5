from datetime import datetime
from typing import List, Union
from pydantic import BaseModel


class NameBaseSchema(BaseModel):
    id: Union[str, None] = None
    title: Union[str, None] = None
    first: str
    family: Union[str, None] = None
    other: Union[str, None] = None
    createdAt: Union[datetime, None] = None
    updatedAt: Union[datetime, None] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class ListNameResponse(BaseModel):
    status: str
    results: int
    names: List[NameBaseSchema]
