# MCP Server Examples

This repository contains two example implementations of Model Context Protocol (MCP) servers, demonstrating how to build simple MCP servers in both Python and TypeScript.

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). MCP servers expose tools, resources, and prompts that can be discovered and used by MCP clients like Claude.

## Examples in this Repository

### 1. Python MCP Server (`python/`)

A minimal MCP server implementation using the Python MCP SDK with FastMCP.

**Features:**

- **Tool:** `add(a, b)` - Adds two numbers together
- **Transport:** StreamableHTTP
- **Framework:** FastMCP (built on Starlette)
- **Health Check:** GET `/health`

**Quick Start:**

```bash
cd python
uv run main.py
```

**Using Docker:**

```bash
cd python
docker build -t python-mcp-server .
docker run -p 9000:9000 python-mcp-server
```

**Dependencies:**

- Python 3.11+
- mcp>=1.0.0
- uv (package manager)

### 2. TypeScript MCP Server (`typescript/`)

A type-safe MCP server implementation using the TypeScript MCP SDK with Express.js.

**Features:**

- **Tool:** `add` - Adds two numbers with Zod schema validation
- **Transport:** StreamableHTTPServerTransport
- **Framework:** Express.js
- **Health Check:** GET `/health`
- **MCP Endpoint:** POST `/mcp`

**Quick Start:**

```bash
cd typescript
npm install
npm run dev
```

**Using Docker:**

```bash
cd typescript
docker build -t typescript-mcp-server .
docker run -p 9000:9000 typescript-mcp-server
```

**Dependencies:**

- Node.js 20+
- @modelcontextprotocol/sdk
- Express.js
- Zod (for schema validation)

## Project Structure

```
obot-mcp-examples/
├── python/
│   ├── main.py              # Server implementation
│   ├── pyproject.toml       # Project configuration
│   ├── Dockerfile           # Container definition
│   └── CLAUDE.md            # Development guidelines
├── typescript/
│   ├── src/
│   │   └── index.ts         # Server implementation
│   ├── package.json         # Project configuration
│   ├── tsconfig.json        # TypeScript config
│   ├── Dockerfile           # Container definition
│   ├── README.md            # Detailed documentation
│   └── CLAUDE.md            # Development guidelines
└── README.md                # This file
```

## Use Cases

These examples demonstrate:
- How to create a basic MCP server
- How to expose tools via MCP
- How to use StreamableHTTP transport
- How to add health check endpoints
- How to containerize MCP servers

## Learn More

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [FastMCP](https://github.com/jlowin/fastmcp)

## License

See individual project directories for license information.
