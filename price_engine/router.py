from .raydium_onchain import RaydiumOnChain
from .fallback_price import FallbackPrice

class PriceRouter:
    def __init__(self, raydium: RaydiumOnChain, fallback: FallbackPrice, raydium_pools):
        self.raydium = raydium
        self.fallback = fallback
        self.raydium_pools = raydium_pools

    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # 🚀 Alleen ORCA via on-chain Raydium
        if symbol == "ORCA":
            price = self.raydium.get_price(symbol)
            if price is not None and price > 0:
                return price

        # 🚀 ALTIJD fallback voor alle andere tokens
        return self.fallback.get_price(symbol)
