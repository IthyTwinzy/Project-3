
from todo_database import DB



def delete_task(input:str):
    
    """Deletes a task from the todo list"""
    isFound = False
    
    task_key = input("Enter the name of the task to delete: ")

    for task_key in DB.data.values():
        if task_key == task_key:
            del DB.data[task_key]
            isFound = True
            return f"Task '{task_key}' deleted successfully."

    return f"Task '{task_key}' not found in the todo list."