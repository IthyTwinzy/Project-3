from todo_database import DB
import sys
import mcp

@mcp.tool() # Defines the function as a tool function, usable by the MCP
def add(task, details, due, dueTime):
    """ Prompts the user four times for input data """
    task = input("Describe the task you want to add briefly ")
    details = input("Describe the task you want to add in detail ")
    due = input("When is it due by? (MONTH/DAY/YEAR Ex. 03/04/2026) ")
    dueTime = input("What time is it due by? (Hour:Minute Ex. 01:50) ")

    # Adds the data which the user input to the database dictionary
    DB.data[task] = {
        "details": details,
        "due date": due,
        "due time": dueTime,
    }
    # Debug
    if task in DB.data:
        sys.stderr.write("Task added") # Alternative to print; this is from the system