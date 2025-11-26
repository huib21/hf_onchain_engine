import requests

class FallbackPrice:
    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # Stablecoins = 1.00
        if symbol in ["USDC", "USDT"]:
            return 1.00

        # BONK + JUP via Helius Token Metadata (werkt in jouw setup)
        url = f"https://api.helius.xyz/v0/token-metadata?api-key=aa7555cc-2d2d-4f84-aa42-799065b84cfc"
        payload = {
            "mintAccounts": [
                # JUP mint
                "JUP4fbU5urY3ZD3w4eRueiMiXo7iioMWhFjtXA3hspBi",
                # BONK mint
                "DezX6n4aR6E3efwAj2bfvELoUXyq5YhZr25G7c8xENSe"
            ]
        }

        try:
            r = requests.post(url, json=payload, timeout=10)
            r.raise_for_status()
            data = r.json()

            # Extract price based on mint
            if symbol == "JUP":
                return data[0].get("price", None)
            if symbol == "BONK":
                return data[1].get("price", None)

        except:
            return None
