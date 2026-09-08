from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.student_exceptions import StudentNotFoundError

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