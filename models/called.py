from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Calleds(SQLModel, table = True):
    id : int = Field(primary_key= True)
    title: str
    description : str
    status : str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())