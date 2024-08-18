from fastapi import APIRouter, Depends
from injector import inject

class RoutingController:
    @inject
    def __init__(self, router: APIRouter):
        self.router = router
        self.setup_routes()

    def setup_routes(self):
        @self.router.get("/health")
        async def say_hello():
            return {"message": "Health from RoutingController"}

        # Add more routes as needed

def create_router() -> APIRouter:
    return APIRouter()
