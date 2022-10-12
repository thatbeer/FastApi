from distutils.sysconfig import customize_compiler
from http.client import responses
from multiprocessing.connection import wait
from fastapi import APIRouter, Cookie , Header , Form
from fastapi.responses import HTMLResponse , PlainTextResponse , Response
from typing import Optional , List
from custom_log import log 
import time

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch','camera','phone']


async def time_consuming_functionality():
    time.sleep(6)
    return "who awake me"


@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get('/all')
def get_all_product():
    ##log("MY API CALL THIS LOG FROM GET ALL PRODUCT")
    #return products
    data = " ".join(products)
    response = Response(content=data,media_type="text_plain")
    response.set_cookie(key="test_cookie",value="test_cookie_value")
    return response


@router.get('/withheader')
def get_products(
    response: Response,
    customize_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
    ):
    #response.headers['custome_response_header'] = " and ".join(customize_header)
    return {'data': products, 'custom_header': customize_header
    ,'my_cookie': test_cookie}




@router.get('/{id}',responses={
    200: {
        "content": {
            "text/html": {
                "example" : "<div>Product</div>"
            }
        },
        "desciption": "returns the html for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "<div>Product not avaible</div>"
            }
        },
        "desciption": "a cleartext error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not aviable"
        return PlainTextResponse(status_code = 404,content=out,media_type='text/plain')
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
            .prodcut {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
    return HTMLResponse(content=out,media_type="text/html")