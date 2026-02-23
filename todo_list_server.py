from mcp.server.fastmcp import FastMCP
from dataclasses import dataclass
import sys
import json 
import os

# SERVER INITIALIZATION
mcp = FastMCP("Todo List Server")

@dataclass
class AppContext:
    """Stores context data used for the todolist"""
    db: dict = None

# Reads from db
def read_db():
    """Gets data from the todo list db"""

    new_db = None
    if os.path.exists("tasks.json"):
        with open("tasks.json", 'r') as task_file:
            new_db: dict = json.load(task_file)
        AppContext.db = new_db
    
# Writes to db
def write_db():
    """Writes data to the database"""
    
    if AppContext.db != None:
        with open("temp.json", 'w') as task_file:
            json.dump(AppContext.db, task_file)
        os.replace("temp.json", "tasks.json")

# Starts the program and handles file recources
if __name__ == "__main__":
    try:
        read_db()
        mcp.run()
    except (KeyboardInterrupt):
        sys.stderr.write("Server exited via keyboard interupt")
    finally:
        write_db()