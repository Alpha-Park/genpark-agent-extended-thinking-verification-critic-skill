import sys
import json
from client import ExtendedThinkingVerificationCritic

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "verify_claims",
                        "description": "Performs extended thinking verification across claims.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "claims_text": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        critic = ExtendedThinkingVerificationCritic()
        res = critic.verify_claims(args.get("claims_text", ""))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    critic = ExtendedThinkingVerificationCritic()
    print(json.dumps(critic.verify_claims(), indent=2))

if __name__ == "__main__":
    main()
