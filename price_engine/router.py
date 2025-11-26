from .raydium_onchain import RaydiumOnChain
from .fallback_price import FallbackPrice

class PriceRouter:
    def __init__(self, raydium: RaydiumOnChain, fallback: FallbackPrice, raydium_pools):
        self.raydium = raydium
        self.fallback = fallback
        self.raydium_pools = raydium_pools

    def get_price(self, symbol: str):
        symbol = symbol.upper()

        # Gebruik Raydium als het token een on-chain USDC pool heeft
        if symbol in self.raydium_pools:
            price = self.raydium.get_price(symbol)
            if price is not None:
                return price

        # Anders fallback
        return self.fallback.get_price(symbol)
