from typing import Dict

from flask import jsonify


def list_habits():
    """
    Return a list of habits
    """
    return jsonify([
        {
            "id": 1,
            "description": "Drink 8 glasses of water a day",
            "user_id": 1,
            "created_at": "2020-01-01 12:00",
            "updated_at": "2020-01-01 12:00",
        },
    ])


def create_habit(body: Dict):
    """
    Create a new habit
    """
    return jsonify({
        "id": 1,
        "description": body["description"],
        "user_id": body["user_id"],
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    }), 201


def get_habit_by_id(habit_id: int):
    """
    Get a habit by ID
    """
    return jsonify({
        "id": habit_id,
        "description": "Drink 8 glasses of water a day",
        "user_id": 1,
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    })


def update_habit(habit_id: int, body: Dict):
    """
    Update a habit
    """
    return jsonify({
        "id": habit_id,
        "description": body["description"],
        "user_id": body["user_id"],
        "created_at": "2020-01-01 12:00",
        "updated_at": "2020-01-01 12:00",
    }), 202


def delete_habit(habit_id: int):
    """
    Delete a habit
    """