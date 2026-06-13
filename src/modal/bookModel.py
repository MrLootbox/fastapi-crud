from typing import Optional
from pydantic import BaseModel, Field

class Book:
    id:str
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self, id:str, title:str, author:str, description:str, rating:int,published_date:int ):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date= published_date


class BookRequest(BaseModel):
    id:Optional[int] = Field(description="ID is not needed on create", default=None)
    title:str = Field(min_length=3, max_length=15)
    author:str = Field(min_length=1,max_length=20)
    description:str = Field(min_length=1, max_length=100)
    rating:int = Field(gt=1, lt=6)
    published_date:int = Field(ge=1000, le=2100)

    model_config={
        "json_schema_extra":{
            "example":{
            "title":"hogwarts legacy",
            "author":"Mahesh",
            "description":"a story about mahesh on hogwarts",
            "rating":5,
            "published_date":2020
            }
        }
    }
