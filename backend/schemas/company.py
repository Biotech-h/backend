from pydantic import BaseModel, Field


class CorrectCompany(BaseModel):

    uid: int
    name: str = Field(min_length=2)
    region: str = Field(min_length=2)
    category: str = Field(min_length=2)
    description: str

    class Config:
        orm_mode = True
