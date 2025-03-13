import logging

from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

# logger setup
logger = logging.getLogger('micro-service')

# dummy database
all_products = ['apple', 'samsung', 'nokia', 'realme', 'vivo']

# initialize router
application_router_v1 = APIRouter()
application_router_v2 = APIRouter()


# application endpoints
# traditional approach using request json body.
@application_router_v1.get("/all-products")
async def get_all_products(request: Request):
    request_data = await request.json()
    logger.info(f'[request data: {request_data}]')
    response = JSONResponse(content=all_products, status_code=200)
    logger.info(f'[response : {all_products}]')
    return response


# path parameter
@application_router_v1.get('/product/{index}')
def get_product_at_specific_index(index: int):
    if index >= len(all_products):
        response = JSONResponse(content='invalid product id', status_code=404)
    else:
        response = JSONResponse(content={'id': index, 'product-name': all_products[index]}, status_code=200)
    logger.info(f'[response: {response.body.decode()}]')
    return response


# query parameter
@application_router_v1.get('/validate')
def validate_product_using_id_and_name(id: int, name: str):
    if id >= len(all_products):
        response = JSONResponse(content='Invalid Product id', status_code=400)
    elif id < len(all_products) and name in all_products:
        is_valid = id == all_products.index(name)
        response = JSONResponse(content={'validate': is_valid}, status_code=200)
    else:
        response = JSONResponse(content="ERROR")
    logger.info(f'[response : {response.body.decode()} ]')
    return response


# request body using pydantic
# in below approach we will validate the request data using pydantic model class
class Product(BaseModel):
    name: str
    id: int
    description: str = 'this is product from company.'


@application_router_v2.post('/validate')
def validate_product(product: Product):
    logger.info(f'product: {product}')
    if product.id >= len(all_products):
        response = JSONResponse(content='Invalid Product id', status_code=400)
    elif product.id < len(all_products) and product.name in all_products:
        is_valid = product.id == all_products.index(product.name)  # validate product information
        response = JSONResponse(content={'validate': is_valid}, status_code=200)
    else:
        response = JSONResponse(content="ERROR")
    logger.info(f'[response : {response.body.decode()} ]')
    return response
