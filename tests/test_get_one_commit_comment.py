import requests


def test_get_one_commit_comment_successfully(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/git-praktis/comments/72467833")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id"] == 72467833


def test_get_one_commit_comment_id_does_not_exist(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/git-praktis/comments/72467000")

    assert response.status_code == 404


def test_get_one_commit_comment_repo_does_not_exist(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/test-repo/comments/72467833")

    assert response.status_code == 404


def test_get_one_commit_comment_user_does_not_exist(base_url):
    response = requests.get(f"{base_url}/repos/chicken/git-praktis/comments/72467833")

    assert response.status_code == 404