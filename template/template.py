from custom_log import log
from fastapi import APIRouter, BackgroundTasks 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse 
from fastapi.requests import Request
from schemas import ProductBase

router = APIRouter(
    prefix='/template',
    tags=['template']
)

templates = Jinja2Templates(directory="template")

@router.get('/products/{id}' , response_class=HTMLResponse)
def get_product(id: str, product: ProductBase,request:  Request, bt: BackgroundTasks):
    bt.add_task(log_template_call,f"Template read for product with id : {id}")
    return templates.TemplateResponse(
        "product.html",{
            "request" : request,
            "id": id
            ,"title": product.title,
            "description" : product.description,
            "price": product.price
        }
    )

def log_template_call(message: str):
    log("My API", message)