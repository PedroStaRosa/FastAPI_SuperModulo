from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class CalledCreate(BaseModel):
    title: str
    description: str
    status: str

    

    @field_validator('status')
    def check_status(cls, value):

        status_list = ["Aberto","Andamento","Concluido"]
        
        if value not in status_list:
            raise ValueError("Status deve ser ABERTO , EM ANDAMENTO OU CONCLUIDO")

        return value 
