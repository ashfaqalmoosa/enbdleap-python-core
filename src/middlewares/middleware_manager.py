from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from typing import List, Type

class MiddlewareManager:
    def __init__(self):
        self.middlewares: List[Type[BaseHTTPMiddleware]] = []

    def add_middleware(self, middleware: Type[BaseHTTPMiddleware]):
        self.middlewares.append(middleware)

    def apply_middlewares(self, app: FastAPI):
        for middleware in self.middlewares:
            app.add_middleware(middleware)
