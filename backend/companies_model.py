from pydantic import BaseModel, Field, PositiveInt
from typing import Optional, List


class CorrectCompany(BaseModel):

    uid: Optional[PositiveInt]
    name: str = Field(min_length=2)
    region: str = Field(min_length=2)
    field_of_activity: str = Field(min_length=2)
    description: Optional[List[str]]
