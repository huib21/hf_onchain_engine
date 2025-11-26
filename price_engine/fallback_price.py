cat > price_engine/fallback_price.py << 'EOF'
import requests

class FallbackPrice:
    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # Stablecoins
        if symbol in ["USDC", "USDT"]:
            return 1.00

        # Global Jupiter price feed
        try:
            url = f"https://api.jup.ag/price/v2?ids={symbol}"
            r = requests.get(url, timeout=2)
            r.raise_for_status()
            data = r.json()

            # Format: {"data": {"SOL": {"price": 188}}}
            return data["data"][symbol]["price"]
        except:
            return None
EOF
