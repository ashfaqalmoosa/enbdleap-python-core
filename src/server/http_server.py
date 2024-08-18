from fastapi import FastAPI, APIRouter
from injector import inject, Module, provider, singleton
from src.routing_controller import RoutingController, create_router
from src.config import AppConfig
from src.middlewares import (
MiddlewareManager , LoggerMiddleware , ErrorHandlerMiddleware
)

class HTTPServer:
    @inject
    def __init__(self, app: FastAPI, config: AppConfig):
        self.app = app
        self.config = config

    def start(self):
        import uvicorn
        uvicorn.run(self.app, host=self.config.APP_HOST, port=self.config.APP_PORT)

class AppModule(Module):
    @singleton
    @provider
    def provide_fastapi(self, controller: RoutingController, middleware_manager: MiddlewareManager, config: AppConfig, ) -> FastAPI:
        app = FastAPI(debug=config.APP_DEBUG, title=config.APP_NAME)
        app.include_router(controller.router)
        middleware_manager.apply_middlewares(app)
        return app

    @singleton
    @provider
    def provide_http_server(self, app: FastAPI, config:AppConfig) -> HTTPServer:
        return HTTPServer(app, config)

    @singleton
    @provider
    def provide_routing_controller(self, router: APIRouter) -> RoutingController:
        return RoutingController(router)

    @singleton
    @provider
    def provide_router(self) -> APIRouter:
        return create_router()

    @singleton
    @provider
    def provide_config(self) -> AppConfig:
        return AppConfig()

    @singleton
    @provider
    def provide_middleware_manager(self) -> MiddlewareManager:
        manager = MiddlewareManager()
        manager.add_middleware(LoggerMiddleware)
        manager.add_middleware(ErrorHandlerMiddleware)
        return manager