from fastapi import APIRouter , status , Response , Depends
from enum import Enum
from helper.helper import required_function

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogType(str,Enum):
    short =  'short'
    story = 'story'
    howto = 'howto'



@router.get('/all' , tags=['blog'] , summary='Retrieve all blog' , 
            description='This api call simulates fetching all blogs')
def get_blog(page = 1,page_size : int | None = None , 
                 req_parameter: dict = Depends(required_function)):
    return {"message":f"ALL {page_size} blogs on pahe {page}",'req' : req_parameter}

@router.get('/{id}/comments/{comment_id}' , tags=['comment'] , response_description="return object" )
def get_comment(id: int,comment_id :int,valid: bool =True,username : str| None = None):
    """Similates retrieveinh a comment of a blog

    Args:
        id (int): blog's id
        comment_id (int): comment's id
        valid (bool, optional): is this comment valid or not. Defaults to True.
        username (str | None, optional): username of the comment poster. Defaults to None.

    Returns:
        _type_: message
    """
    return {"message" : f"blog_id {id} , comment_id {comment_id} m valid {valid} , username {username}"}

@router.get('/type/{type}' , tags=['blog'])
def get_blog_type(type:str):
    return {'message' : f"Blog type {type}"}

@router.get('/{id}', status_code=status.HTTP_200_OK )
def get_blog_id(id:int, response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'Blog {id} not Found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
    
    
    
    


