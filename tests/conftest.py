import pytest


@pytest.fixture
def base_url():
    return 'https://api.github.com'


@pytest.fixture
def update_comment_req_body():
    return {
        "body": "this is an edit"
    }


@pytest.fixture
def create_commit_req_body():
    return {
        "body": "too-tired-of-this",
        "path": "/README.md",
        "position": 4
    }
