# tests/test_app.py
import pytest
from myapp import app, workouts


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    workouts.clear()  # isolate tests
    with app.test_client() as c:
        yield c

def test_get_index(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Log a workout" in r.data

def test_post_add_valid(client):
    r = client.post("/", data={"workout": "Run", "duration": "30"}, follow_redirects=True)
    assert r.status_code == 200
    assert any(w["workout"] == "Run" and w["duration"] == 30 for w in workouts)
    assert b"Successfully added" in r.data

def test_post_missing_fields(client):
    r = client.post("/", data={"workout": "", "duration": ""}, follow_redirects=True)
    assert r.status_code == 200
    assert b"Please enter both" in r.data

def test_post_non_numeric_duration(client):
    r = client.post("/", data={"workout": "Swim", "duration": "abc"}, follow_redirects=True)
    assert r.status_code == 200
    assert b"Duration must be a number." in r.data
