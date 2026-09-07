from fastapi import FastAPI

from routes.students import router as student_router


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }


app.include_router(student_router)