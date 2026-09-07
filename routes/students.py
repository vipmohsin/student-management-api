from fastapi import APIRouter, HTTPException

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
    student = service.get_student_by_roll(roll_no)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{roll_no}")
def update_student(roll_no: int, student_data: StudentCreate):
    student = service.update_student(
        roll_no,
        student_data.name,
        student_data.age,
        student_data.marks
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.delete("/{roll_no}")
def delete_student(roll_no: int):
    result = service.delete_student(roll_no)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }