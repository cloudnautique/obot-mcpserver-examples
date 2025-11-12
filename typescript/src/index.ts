import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import express from 'express';
import { z } from 'zod';

const port = parseInt(process.env.PORT || '9000');

const app = express();
app.use(express.json());

const server = new McpServer({
    name: 'add-numbers-server',
    version: '1.0.0'
});

server.registerTool(
    'add',
    {
        title: 'Add Numbers',
        description: 'Add two numbers together',
        inputSchema: {
            a: z.number().describe('First number'),
            b: z.number().describe('Second number')
        },
        outputSchema: {
            result: z.number()
        }
    },
    async ({ a, b }) => {
        const output = { result: a + b };
        return {
            content: [{ type: 'text', text: JSON.stringify(output) }],
            structuredContent: output
        };
    }
);

app.post('/mcp', async (req, res) => {
    const transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: undefined,
        enableJsonResponse: true
    });

    res.on('close', () => {
        transport.close();
    });

    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
});

app.get('/health', (req, res) => {
    res.status(200).json({ status: 'ok' });
});

app.listen(port, () => {
    console.log(`MCP Server running on http://localhost:${port}/mcp`);
    console.log(`Health check available at http://localhost:${port}/health`);
}).on('error', (error) => {
    console.error('Server error:', error);
    process.exit(1);
});
