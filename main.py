from fastapi import FastAPI,HTTPException
from student import Student
from schemas import StudentCreate
app = FastAPI()

students=[
    Student(101,"mohsin",18,90),
    Student(102,"hassan",17,90),
    Student(103,"mazher",21,90)
    
]
next_roll_no=104
@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }

@app.get("/students")
def get_students():
    return students   

@app.post("/students")
def create_student(student_data : StudentCreate):
    global next_roll_no

    student=Student(
        roll_no=next_roll_no,
        name=student_data.name,
        age=student_data.age,
        marks=student_data.marks
    )
    
    students.append(student)
    next_roll_no +=1
    return student

@app.get("/students/{roll_no}")
def get_student(roll_no: int):
    for student in students:
        if student.roll_no == roll_no:
            return student
        
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    

@app.put("/students/{roll_no}")
def update_student(roll_no:int, student_data : StudentCreate):
    for student in students:
        if student.roll_no == roll_no:
            student.name = student_data.name
            student.age=student_data.age
            student.marks= student_data.marks

            return student
        
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.delete("/students/{roll_no}")
def delete_student(roll_no: int):

    for student in students:
        if student.roll_no == roll_no:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )    