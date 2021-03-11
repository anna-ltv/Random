import requests

def test_status_code_200():
    response = requests.get("https://my-json-server.typicode.com/typicode/demo")
    assert response.status_code == 200
    assert response.status_code != 400

def test_add_new_post():
    data = { "id": 4, "title": "Post 4"}
    new_post = requests.post("https://my-json-server.typicode.com/typicode/demo/posts", data = data)
    assert new_post.status_code == 201 #статус 201 - Created
