from .fallback_price import FallbackPrice
from .raydium_onchain import RaydiumOnChain

class PriceRouter:
    def __init__(self, raydium: RaydiumOnChain, fallback: FallbackPrice, raydium_pools):
        self.raydium = raydium
        self.fallback = fallback
        self.raydium_pools = raydium_pools

    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # 1️⃣ Raydium ONLY for ORCA (en later SOL/ETH/RAY wanneer node fix klaar is)
        if symbol == "ORCA":
            price = self.raydium.get_price(symbol)
            if price is not None:
                return price

        # 2️⃣ ALLES ANDERS → DIRECT NAAR FALLBACK
        return self.fallback.get_price(symbol)
