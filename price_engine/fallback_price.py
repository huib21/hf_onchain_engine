import requests

class FallbackPrice:
    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # Stablecoins = 1.00
        if symbol in ["USDC", "USDT"]:
            return 1.00

        # Gebruik Jupiter v6 (100% werkt in jouw node)
        url = f"https://api.jup.ag/price/v2?ids={symbol}"

        try:
            r = requests.get(url, timeout=2)
            r.raise_for_status()
            data = r.json()

            if symbol in data and "price" in data[symbol]:
                return float(data[symbol]["price"])

        except:
            return None

        return None
