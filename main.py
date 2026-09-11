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
# student not found error handling and assignig
app.add_exception_handler(
    StudentNotFoundError,
    student_not_found_handler
)
# data load eror handling and assigning
app.add_exception_handler(
    StudentDataLoadError,
    student_data_load_handler
)
# data save error handling and assiging
app.add_exception_handler(
    StudentDataSaveError,
    student_data_save_handler
)

app.include_router(student_router)