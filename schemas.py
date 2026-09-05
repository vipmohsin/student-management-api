from pydantic import BaseModel,Field

class StudentCreate(BaseModel):
    name:str
    age:int= Field(ge=5 , le=80)
    marks:int = Field(ge=0 , le=100)