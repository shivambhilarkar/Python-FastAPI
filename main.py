import logging
from fastapi import FastAPI
from app.app_middleware import LoggingMiddleWare
from app.controller import application_router_v1, application_router_v2

# logger setup
logger = logging.getLogger('micro-service')


# application setup
app = FastAPI(title='demo application', version='1.0.0')
logger.info(f'[application has been started.]')

# add middleware to application
app.add_middleware(LoggingMiddleWare)

# add router to application
app.include_router(application_router_v1)
app.include_router(application_router_v2)