from injector import Injector
from src.server.http_server import AppModule, HTTPServer

def main():
    injector = Injector([AppModule()])
    server = injector.get(HTTPServer)
    server.start()

if __name__ == "__main__":
    main()


# from fastapi import FastAPI
# from enbdleap_core.routing_controller import RoutingController
# from enbdleap_core.middleware import MiddlewareManager, LoggerMiddleware, ErrorHandlerMiddleware
# from enbdleap_core.config import AppConfig
# from enbdleap_core.http_server import HTTPServer
# from enbdleap_core.routing_controller import create_router
# from fastapi import APIRouter
#
# def create_app() -> FastAPI:
#     config = AppConfig()
#     router = create_router()
#     middleware_manager = MiddlewareManager()
#
#     # Add middlewares
#     middleware_manager.add_middleware(LoggerMiddleware)
#     middleware_manager.add_middleware(ErrorHandlerMiddleware)
#
#     # Set up the routing controller with middleware
#     controller = RoutingController(router, middleware_manager)
#
#     # Create the FastAPI app
#     app = FastAPI(debug=config.DEBUG, title=config.APP_NAME)
#     app.include_router(controller.router)
#
#     # Apply middlewares
#     middleware_manager.apply_middlewares(app)
#
#     return app
#
# def main():
#     app = create_app()
#     server = HTTPServer(app, AppConfig())
#     server.start()
#
# if __name__ == "__main__":
#     main()