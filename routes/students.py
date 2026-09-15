from fastapi import APIRouter,Depends

from dependencies import get_student_service
from schemas import StudentCreate,StudentResponse
from services.student_service import StudentService
from repositories.student_repository import StudentRepository


router = APIRouter(prefix="/students", tags=["Students"])


# 
@router.get(
    "/",
    response_model=list[StudentResponse]
    )
def get_students(service: StudentService = Depends(get_student_service)):

    return service.get_all_students()


@router.post(
    "/",
    response_model=StudentResponse
    )
def create_student(student_data: StudentCreate,service: StudentService = Depends(get_student_service)):
    
    return service.create_student(
        student_data.name,
        student_data.age,
        student_data.marks
    )


@router.get(
    "/{roll_no}",
    response_model=StudentResponse
    )
def get_student(roll_no: int, service: StudentService = Depends(get_student_service)):
    
    return service.get_student_by_roll(roll_no)


@router.put(
    "/{roll_no}",
    response_model=StudentResponse
    )
def update_student(roll_no: int, student_data: StudentCreate, service: StudentService = Depends(get_student_service)):
    
    return service.update_student(
        roll_no,
        student_data.name,
        student_data.age,
        student_data.marks
    )


@router.delete("/{roll_no}")
def delete_student(roll_no: int, service: StudentService = Depends(get_student_service)):
    
    service.delete_student(roll_no)

    return {
        "message": "Student deleted successfully"
    }