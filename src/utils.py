"""Utility file."""

from fastapi.responses import JSONResponse


def normalize_response(data, status_code=200):
    return JSONResponse(content={"data": data}, status_code=status_code)
