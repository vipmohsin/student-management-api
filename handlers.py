from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.student_exceptions import (
    StudentNotFoundError,
    StudentDataLoadError,
    StudentDataSaveError
)

async def student_not_found_handler(
    request: Request,
    exc: StudentNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc)
        }
    )
    
async def student_data_load_handler(
    request: Request,
    exc : StudentDataLoadError
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Student data could not be loaded"
        }
        
    ) 
       
async def student_data_save_handler(
    request: Request,
    exc : StudentDataLoadError
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Student data could not be saved"
        }
        
    )    