import pytest

from habit_tracker.app import create_app


def test_can_create_app():
    app = create_app()
    assert app is not None


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client


def test_list_habits(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == [
        {
            "id": 1,
            "description": "Drink 8 glasses of water a day",
            "user_id": 1,
            "created_at": "2020-01-01 12:00",
            "updated_at": "2020-01-01 12:00",
        },
    ]


def test_create_habit(client):
    payload = {
        "description": "Drink 8 glasses of water a day",
        "user_id": 1,
    }
    response = client.post("/", json=payload)
    assert response.status_code == 201
    assert response.json == {
        "id": 1,
        "description": "Drink 8 glasses of water a day",
        "user_id": 1,
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    }


def test_get_habit_by_id(client):
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "description": "Drink 8 glasses of water a day",
        "user_id": 1,
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    }


def test_update_habit(client):
    payload = {
        "description": "Workout 45 minutes a day",
        "user_id": 1,
    }
    response = client.put("/1", json=payload)
    assert response.status_code == 202
    assert response.json == {
        "id": 1,
        "description": "Workout 45 minutes a day",
        "user_id": 1,
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    }


def test_delete_habit(client):
    response = client.delete("/1")
    assert response.status_code == 204
