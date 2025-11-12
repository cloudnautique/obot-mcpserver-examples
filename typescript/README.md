# MCP Add Numbers Server

A Model Context Protocol (MCP) server that provides a tool to add two numbers.

## Features

- MCP tool: `add` - Adds two numbers together
- HTTP streamable transport
- Health check endpoint
- Configurable port via environment variable
- Docker support

## Installation

```bash
npm install
```

## Development

```bash
npm run dev
```

## Build

```bash
npm run build
```

## Run

```bash
npm start
```

## Configuration

- `PORT` environment variable (default: 9000)

## Endpoints

- `POST /mcp` - MCP endpoint for tool calls
- `GET /health` - Health check endpoint

## Docker

Build the image:

```bash
docker build -t mcp-add-server .
```

Run the container:

```bash
docker run -p 9000:9000 mcp-add-server
```

With custom port:

```bash
docker run -p 8080:8080 -e PORT=8080 mcp-add-server
```

## Usage Example

Initialize the MCP session:

```bash
curl -X POST http://localhost:9000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}'
```

List available tools:

```bash
curl -X POST http://localhost:9000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

Call the add tool:

```bash
curl -X POST http://localhost:9000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add","arguments":{"a":42,"b":58}}}'
```

Response:

```json
{
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"result\":100}"
      }
    ],
    "structuredContent": {
      "result": 100
    }
  },
  "jsonrpc": "2.0",
  "id": 3
}
```

## Health Check

```bash
curl http://localhost:9000/health
```

Response:

```json
{
  "status": "ok"
}
```
