# MCP Protocol Test Server (Smithery-compatible)

Implements `initialize`, `tools/list`, `tools/call` for MCP JSON-RPC.

## How to run
pip install -r requirements.txt
uvicorn app:app --reload

## Docker build/run
docker build -t mcp-test .
docker run -p 8081:8081 mcp-test

## How to test

### List tools
curl -X POST http://localhost:8081/ -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

### Call add
curl -X POST http://localhost:8081/ -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"add","arguments":{"a":3,"b":2}},"id":2}'

### Call minus
curl -X POST http://localhost:8081/ -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"minus","arguments":{"a":5,"b":1}},"id":3}'
