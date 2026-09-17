from pydantic import BaseModel,Field, field_validator

class StudentCreate(BaseModel):
    name:str = Field(
        min_length=3,
        pattern=r"^[A-Za-z ]+$"
    )
    age:int= Field(ge=5 , le=80)
    marks:float = Field(ge=0 , le=100)
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value.replace(" ", "")) < 3:
            raise ValueError("Name must contain at least 3 letters.")

        return value

class StudentResponse(BaseModel):
    roll_no: int
    name: str
    age: int
    marks: float