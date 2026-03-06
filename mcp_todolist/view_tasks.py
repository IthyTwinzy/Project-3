from todo_database import DB
import json

def view_tasks() -> list[str]:
    """Gets a array containing all tasks in the database"""
    return [f"\"{key}\": {json.dumps(value)}" for key, value in DB.data.items()]