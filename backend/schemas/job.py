from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class CorrectJob(BaseModel):

    uid: int
    name: str = Field(min_length=2)
    company_uid: int = Field(ge=1)
    salary: Optional[int]
    description: Optional[str] = Field(max_length=4000)
    date_published: Optional[date]
    date_expiring: Optional[date]
    url: str

    class Config:
        orm_mode = True
