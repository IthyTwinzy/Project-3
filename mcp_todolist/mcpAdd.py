from todo_database import DB
from typing import Annotated

def add_task(
        task: Annotated[str, "A brief task description i.e. 'Laundry', used as the key for each entry in the dictionary"],
        details: Annotated[str, "A detailed task description i.e. 'Wash clothes, dry clothes, fold clothes'"],
        due: Annotated[str, "The due date (Format: Month/Day/Year, Ex. 03/04/2026)"],
        dueTime: Annotated[str, "The time due (Ex. 14:00)"]) -> str:
    """ Inputs the task into the database using the data provided for this function """

    # Adds the data which the user input to the database dictionary
    DB.data[task] = {
        "details": details,
        "due date": due,
        "due time": dueTime,
    }
    # Debug
    if task in DB.data:
        return "Task added"
    return "Add failed"