from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class CorrectJob(BaseModel):

    uid: int = Field(ge=1)
    name: str = Field(min_length=2)
    company_uid: int = Field(ge=1)
    salary: Optional[int]
    description: str = Field(max_length=100)
    date_published: date
    date_expiring: date
    url: str

    class Config:
        orm_mode = True
