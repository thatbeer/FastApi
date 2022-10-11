from fastapi import APIRouter, Query , Body , Path
from typing import List, Optional
from Model.blog import BlogModel 

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/')
def create_blog(blog : BlogModel, id :int,version : int = 1):
    return {
        "id" : id,
        "data" : blog,
        "version" : version
    }
    
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog : BlogModel , id: int , 
                   comment_title: str = Query(
                       None,
                       title='id of the comment',
                       description='Some description from comment_id',
                       alias='commentId',
                       deprecated=True
                       ), 
                   content : str = Body(...
                                        ,min_length=10
                                        ,max_length=80
                                        ,regex='^[a-z\s]*$'
                                        ),
                   v : Optional[List[str]] = Query(['1.0','1.1','1.2']),
                   comment_id : int = Path(None, gt=5, le=100)
                   ):
    return {
        'blog' : blog,
        'id' : id,
        'comment_title' : comment_title,
        'comment_id' : comment_id,
        'content' : content,
        'version': v
        
    }
    

def required_function():
    return {'message' : 'Learning FASTAPI'}