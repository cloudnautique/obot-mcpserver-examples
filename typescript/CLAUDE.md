# Typescript MCP Server development

Use context7 to read docs if available for libraries.

## Package management with npm

Use uv exclusively for package management in this project.
All deps must be installed using npm
Favor fewer dependencies, make sure you are using the libraries as intended

## MCP server

Always use the official https://github.com/modelcontextprotocol/typescript-sdk SDK
Always use streamable HTTP transport by default
provide a way to specify port via env var. Set the default to 9000
always add a `/health` check on the same port.

## Docker

The command should start the server must start the server