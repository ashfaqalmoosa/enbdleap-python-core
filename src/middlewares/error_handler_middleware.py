import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            logger = logging.getLogger("ErrorHandlerMiddleware")
            logger.error(f"An error occurred: {e}")
            return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})