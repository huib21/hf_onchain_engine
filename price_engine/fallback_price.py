import requests
import subprocess
import json

class FallbackPrice:
    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # stablecoins
        if symbol in ["USDC", "USDT"]:
            return 1.00

        # --- TRY 1: Jupiter v6 (beste endpoint) ---
        try:
            url = f"https://api.jup.ag/price/v6?ids[]={symbol}"
            r = requests.get(url, timeout=2)
            data = r.json()

            if (
                "data" in data
                and symbol in data["data"]
                and "price" in data["data"][symbol]
            ):
                return float(data["data"][symbol]["price"])
        except:
            pass

        # --- TRY 2: fallback via curl (werkt zelfs bij SSL problemen) ---
        try:
            raw = subprocess.check_output(
                ["curl", "-s", f"https://api.jup.ag/price/v6?ids[]={symbol}"]
            )
            data = json.loads(raw.decode("utf-8"))

            if (
                "data" in data
                and symbol in data["data"]
                and "price" in data["data"][symbol]
            ):
                return float(data["data"][symbol]["price"])

        except:
            return None

        return None
