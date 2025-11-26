import requests
from typing import Any, Dict

class HeliusRPC:
    def __init__(self, url: str):
        self.url = url

    def call(self, method: str, params: list) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }

        r = requests.post(self.url, json=payload, timeout=10)
        r.raise_for_status()
        return r.json()
