from mcp.server.fastmcp import FastMCP
import sys

from todo_database import DB
from view_tasks import view_tasks

# Initializes the server
mcp = FastMCP("Todo List Server")

# Sets up all tools needed for the server
mcp.add_tool(view_tasks)

# Starts the server
if __name__ == "__main__":
    try:
        sys.stderr.write("Server started\n")
        mcp.run()
    except (KeyboardInterrupt):
        sys.stderr.write("Server exited via keyboard interupt\n")