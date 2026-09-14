from pydantic import BaseModel,Field

class StudentCreate(BaseModel):
    name:str
    age:int= Field(ge=5 , le=80)
    marks:float = Field(ge=0 , le=100)
    

class StudentResponse(BaseModel):
    roll_no: int
    name: str
    age: int
    marks: float