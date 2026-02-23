from mcp.server.fastmcp import FastMCP
from contextlib import asynccontextmanager
from dataclasses import dataclass

@dataclass
class AppContext:
    """Stores global data used for the todolist"""
    task_db: dict

@asynccontextmanager
async def app_lifespan():
    """Manages the todo list database"""
    data: dict = None # Get json from database

    try:
        yield AppContext(task_db = data)
    finally:
        pass# Close the database
    
# Creates the Server
mcp = FastMCP("Todo List Server", lifespan=app_lifespan)