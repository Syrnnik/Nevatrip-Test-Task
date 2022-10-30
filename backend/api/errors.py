from fastapi import HTTPException


def NotFound404(detail: str):
    return HTTPException(
        status_code=404,
        detail=detail
    )


def WrongDateTimeFormat(detail):
    return HTTPException(
        status_code=400,
        detail=detail
    )
