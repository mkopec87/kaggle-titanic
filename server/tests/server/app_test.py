import pytest

import server


@pytest.fixture()
def client():
    app = server.app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_root(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert resp.data == b"Hi!"


def test_get_version(client):
    resp = client.get("/version")

    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert "Version" in resp.json


def test_post_classify(client):
    resp = client.get("/classify")

    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert "Survived" in resp.json
    assert resp.json["Survived"] in {0, 1}
