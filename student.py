class Student:
    def __init__(self,roll_no,name,age,marks):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.marks=marks
    
    def to_dict(self):
            return{
                "roll_no": self.roll_no,
                "name": self.name,
                "age": self.age,
                "marks": self.marks
            }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["roll_no"],
            data["name"],
            data["age"],
            data["marks"]
        )
        