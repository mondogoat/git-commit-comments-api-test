import requests


def test_get_all_commit_comments_successfully(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/git-praktis/comments")
    assert response.status_code == 200


def test_get_all_commit_comments_from_project_with_no_commit_comments(base_url):
    response = requests.get(f"{base_url}/repos/mondogoat/robot-appium/comments")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body == []
