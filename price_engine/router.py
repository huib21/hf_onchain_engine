from .raydium_onchain import RaydiumOnChain

class PriceRouter:
    def __init__(self, raydium: RaydiumOnChain):
        self.raydium = raydium

    def get_price(self, symbol: str):
        price = self.raydium.get_price(symbol)
        return price
