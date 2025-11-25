import requests
from price_engine.config import HELIUS_API_KEY

class HeliusRPC:
    def __init__(self):
        self.url = f"https://mainnet.helius-rpc.com/?api-key={aa7555cc-2d2d-4f84-aa42-799065b84cfc}"

    def get_account(self, pubkey: str):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [pubkey, {"encoding": "base64"}]
        }
        response = requests.post(self.url, json=payload)
        return response.json()

    def get_multiple_accounts(self, accounts):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getMultipleAccounts",
            "params": [accounts, {"encoding": "base64"}]
        }
        response = requests.post(self.url, json=payload)
        return response.json()
