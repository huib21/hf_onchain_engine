import requests

class JupiterPrice:
    def get_price(self, symbol: str):
        url = f"https://price.jup.ag/v4/price?ids={symbol.upper()}"
        r = requests.get(url, timeout=5)

        if r.status_code != 200:
            return None

        data = r.json().get("data", {})
        return data.get(symbol.upper(), {}).get("price", None)
