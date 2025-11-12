import os
from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

# Get port from environment variable, default to 9000
PORT = int(os.environ.get("PORT", "9000"))

# Create MCP server
mcp = FastMCP("Calculator Service")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.custom_route(path="/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse({"status": "healthy", "service": "Calculator Service"})


if __name__ == "__main__":
    # Configure server settings
    mcp.settings.port = PORT

    # Run server with streamable HTTP transport
    mcp.run(transport="streamable-http")
