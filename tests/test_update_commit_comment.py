import requests

"""
not sure if this is still the endpoint for update. throws 400 even when pasting the exact curl, it throws a 404. 
checking on the network in chrome developer tools, updating a comment calls a put method
"""


def test_update_commit_comment_successfully(base_url, update_comment_req_body):
    response = requests.patch(f"{base_url}/repos/mondogoat/git-praktis/comments/72467833", json=update_comment_req_body)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["body"] == update_comment_req_body["body"]


def test_update_commit_comment_id_does_not_exist(base_url, update_comment_req_body):
    response = requests.patch(f"{base_url}/repos/mondogoat/git-praktis/comments/73111", json=update_comment_req_body)

    assert response.status_code == 404


