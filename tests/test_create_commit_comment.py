import requests

"""same issue as update_commit_comment endpoint. """


def test_create_commit_comment_successfully(base_url, create_commit_req_body):
    response = requests.post(
        f"{base_url}/repos/mondogoat/git-praktis/commits/770b1a76ce924df5d9a08e85e97b1fd9cb9f053a/comments")

    assert response.status_code == 200


def test_create_commit_comment_sha_does_not_exist(base_url, create_commit_req_body):
    response = requests.post(
        f"{base_url}/repos/mondogoat/git-praktis/commits/770b1a76ce924df5d9a08e85e97b1fd9cb9f053a/comments")

    assert response.status_code == 404
