from fastapi import HTTPException, status

def not_found_exception(resource: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource} not found"
    )

def invalid_credential():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credentials"
    )