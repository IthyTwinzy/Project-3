from mcp.server.fastmcp import FastMCP
import sys

from todo_database import DB
from delete import delete_task
from view_tasks import view_tasks
from mcpAdd import add_task

# Initializes the server
mcp = FastMCP("Todo List Server")
    
# Sets up all tools needed for the server
mcp.add_tool(view_tasks)
mcp.add_tool(delete_task)
mcp.add_tool(add_task)

# Starts the server
if __name__ == "__main__":
    try:
        sys.stderr.write("Server started\n")
        mcp.run()
    except (KeyboardInterrupt):
        sys.stderr.write("Server exited via keyboard interupt\n")