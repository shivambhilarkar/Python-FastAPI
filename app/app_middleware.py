
import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from stopwatch import Stopwatch

# logger setup
logger = logging.getLogger('app_middleware')

"""
A "middleware" is a function that works with every request 
before it is processed by any specific path operation. 
And also with every response before returning it.
"""

class LoggingMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) :
        # log the request details
        stopwatch = Stopwatch()
        stopwatch.start()
        request_data = await request.json()
        logger.info(f'[route: {request.url}')
        logger.info(f'[request details : {request_data}]')

        # process the request
        response = await call_next(request)

        # log the response details
        logger.info(f'[request completed in : { round(stopwatch.elapsed, 5)}.ms]')
        logger.info(f'[response details : {response.status_code} ]')
        return response