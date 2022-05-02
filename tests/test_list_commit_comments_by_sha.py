import requests


def test_list_commit_comments_by_sha_successfully(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/git-praktis/commits/770b1a76ce924df5d9a08e85e97b1fd9cb9f053a/comments")

    assert response.status_code == 200


def test_list_commit_comments_sha_does_not_exist(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/git-praktis/commits/770b1a76ce924df5d9a08e85e97b1fd9cb900000/comments")

    assert response.status_code == 404