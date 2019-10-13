from blog_api import api
from flask import json

def test_blog_post():        
    response = api.test_client().post(
        '/api/post',
        data=json.dumps({'title': '1', 'body': '2', 'author': '3'}),
        content_type='application/json',
    )

    assert response.status_code == 200
    assert response.data == b'1 posted successfully!'

def test_comment_post():        
    response = api.test_client().post(
        '/api/comment/0',
        data=json.dumps({'body': '2', 'author': '3'}),
        content_type='application/json',
    )

    assert response.status_code == 200
    assert response.data == b'comment posted successfully!'

def test_blog_get():
    response = api.test_client().get(
        '/api/post/0'
    )
    print(response.data)
    assert response.status_code == 200
    assert b'"title":"1"' in response.data
    assert b'"body":"2"' in response.data
    assert b'"author":"3"' in response.data

def test_comment_get():
    response = api.test_client().get(
        '/api/comment/0'
    )
    print(response.data)
    assert response.status_code == 200
    assert b'"body":"2"' in response.data
    assert b'"author":"3"' in response.data


if __name__ == '__main__':
    test_blog_post()
    test_comment_post()
    test_blog_get()
    test_comment_get()