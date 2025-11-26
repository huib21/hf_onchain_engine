from .fallback_price import FallbackPrice
from .raydium_onchain import RaydiumOnChain

class PriceRouter:
    def __init__(self, raydium: RaydiumOnChain, fallback: FallbackPrice, raydium_pools):
        self.raydium = raydium
        self.fallback = fallback
        self.raydium_pools = raydium_pools

    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # 1️⃣ Alleen ORCA proberen on-chain (optioneel)
        if symbol == "ORCA":
            price = self.raydium.get_price(symbol)
            if price is not None and price > 0:
                return price

        # 2️⃣ ALLES → fallback
        return self.fallback.get_price(symbol)
