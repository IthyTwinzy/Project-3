from mcp.server.fastmcp import FastMCP
import sys

from todo_database import DB
from mcp_todolist.delete_task import delete_task

# Initializes the server
mcp = FastMCP("Todo List Server")

mcp.add_tool(delete_task)
    
# Starts the server
if __name__ == "__main__":
    try:
        sys.stderr.write("Server started\n")
        mcp.run()
    except (KeyboardInterrupt):
        sys.stderr.write("Server exited via keyboard interupt\n")