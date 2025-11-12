import contextlib
import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

# Get host and port from environment variables
HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", "9000"))

# Create MCP server
mcp = FastMCP("Calculator Service")

# Configure to serve at root of mount path (e.g., /mcp instead of /mcp/mcp)
mcp.settings.streamable_http_path = "/"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# Health check endpoint
async def health_check(request: Request) -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse({"status": "healthy", "service": "Calculator Service"})


# Create lifespan manager for the MCP session
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with mcp.session_manager.run():
        yield


# Create Starlette app with both MCP and health endpoints
app = Starlette(
    routes=[
        Route("/health", health_check, methods=["GET"]),
        Mount("/mcp", app=mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)


if __name__ == "__main__":
    # Run with uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
