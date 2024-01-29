from pydantic import BaseModel


class Article(BaseModel):
    url: str
    text: str