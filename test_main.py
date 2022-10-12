from codecs import ascii_encode
from os import access
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200
    
    
def test_auth_error():
    response = client.post("/token",
                           data={"username:": "","password":""})
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")[0].get("msg")
    assert message == ""
def test_auth_success():
    response = client.post("/token",
                           data={"username:": "","password":""})
    access_token = response.json().get("access_token")
    assert access_token

def test_post_article():
    auth = client.post("/token",
                           data={"username:": "","password":""})
    auth_token = auth.json().get("access_token")
    assert auth_token
    
    response = client.post(
        "/article/",
        json={
            "title": "Test article",
            "content": "Test content",
            "published": True,
            "creator_id": 1
        },
        headers= {
            "Authorization": "bearer" + auth_token
        }
    )
    assert response.status_code == 200
    assert response.json().get("title") == "Test article"