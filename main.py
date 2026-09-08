from fastapi import FastAPI

from routes.students import router as student_router
from exceptions.student_exceptions import (
    StudentNotFoundError,
    StudentDataLoadError,
    StudentDataSaveError
)

from handlers import (
    student_not_found_handler,
    student_data_load_handler,
    student_data_save_handler
    
)

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
app.add_exception_handler(
    StudentDataLoadError,
    student_data_load_handler
)
app.add_exception_handler(
    StudentDataSaveError,
    student_data_save_handler
)

app.include_router(student_router)