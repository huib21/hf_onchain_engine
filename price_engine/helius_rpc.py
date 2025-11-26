import requests
from typing import Any, Dict

class HeliusRPC:
    def __init__(self, url: str):
        self.url = url

    def call(self, method: str, params: list, timeout: float = 0.3) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }

        try:
            r = requests.post(self.url, json=payload, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except Exception:
            return None
