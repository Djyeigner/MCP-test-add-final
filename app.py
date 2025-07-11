from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

TOOLS = [
    {
        "name": "add",
        "description": "두 수를 더합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "minus",
        "description": "a에서 b를 뺍니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    }
]

@app.post("/")
async def mcp_rpc(request: Request):
    data = await request.json()
    method = data.get("method")
    req_id = data.get("id")
    params = data.get("params", {})

    if method == "initialize":
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"status": "ok"}
        })

    if method == "tools/list":
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": TOOLS
        })

    if method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        if tool_name == "add":
            a = tool_args.get("a")
            b = tool_args.get("b")
            result = a + b
        elif tool_name == "minus":
            a = tool_args.get("a")
            b = tool_args.get("b")
            result = a - b
        else:
            return JSONResponse({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": "Unknown tool"}
            })
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": result
        })

    return JSONResponse({
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": "Method not found"}
    })
