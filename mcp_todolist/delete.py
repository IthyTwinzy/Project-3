
from todo_database import DB

def delete_task(input:str):
    
    """Deletes a task from the todo list"""
    if input in DB.data:
        del DB.data[input]
        return f"Task '{input}' deleted successfully."

    return f"Task '{input}' not found in the todo list."