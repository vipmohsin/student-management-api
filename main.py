from fastapi import FastAPI

from routes.students import router as student_router
from exceptions.student_exceptions import StudentNotFoundError
from handlers import student_not_found_handler

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }

app.add_exception_handler(
    StudentNotFoundError,
    student_not_found_handler
)

app.include_router(student_router)