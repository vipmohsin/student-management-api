from fastapi import APIRouter

from schemas import StudentCreate
from services.student_service import StudentService
from repositories.student_repository import StudentRepository


router = APIRouter(prefix="/students", tags=["Students"])

repo = StudentRepository()
service = StudentService(repo)

@router.get("/")
def get_students():
    return service.get_all_students()


@router.post("/")
def create_student(student_data: StudentCreate):
    return service.create_student(
        student_data.name,
        student_data.age,
        student_data.marks
    )


@router.get("/{roll_no}")
def get_student(roll_no: int):
    return service.get_student_by_roll(roll_no)


@router.put("/{roll_no}")
def update_student(roll_no: int, student_data: StudentCreate):
    return service.update_student(
        roll_no,
        student_data.name,
        student_data.age,
        student_data.marks
    )


@router.delete("/{roll_no}")
def delete_student(roll_no: int):
    service.delete_student(roll_no)

    return {
        "message": "Student deleted successfully"
    }