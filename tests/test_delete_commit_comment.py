import requests

"""same issue as update_commit_comment endpoint. """


def test_delete_commit_comment_successfully(base_url):
    response = requests.delete(f"{base_url}/repos/mondogoat/git-praktis/comments/72523553")

    assert response.status_code == 204


def test_delete_commit_comment_does_not_exist(base_url):
    response = requests.delete(f"{base_url}/repos/mondogoat/git-praktis/comments/000000")
    assert response.status_code == 404
