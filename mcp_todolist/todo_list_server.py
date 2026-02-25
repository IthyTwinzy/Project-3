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
    if os.path.exists("output/tasks.json"):
        with open("output/tasks.json", 'r') as task_file:
            new_db: dict = json.load(task_file)
        AppContext.db = new_db
    
# Writes to db
def write_db():
    """Writes data to the database"""
    
    # Creates the output directory
    if not os.path.exists("output"):
        os.mkdir("output")

    with open("output/temp.json", 'w') as task_file:
        json.dump(AppContext.db, task_file)
    os.replace("output/temp.json", "output/tasks.json")

# Starts the program and handles file recources
if __name__ == "__main__":
    try:
        read_db()
        sys.stderr.write("Server started\n")
        mcp.run()
    except (KeyboardInterrupt):
        sys.stderr.write("Server exited via keyboard interupt\n")
    finally:
        write_db()