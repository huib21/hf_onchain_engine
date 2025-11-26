from price_engine.raydium_onchain import RaydiumOnChain
from price_engine.jupiter_price import JupiterPrice

class PriceRouter:
    def __init__(self):
        self.raydium = RaydiumOnChain()
        self.jupiter = JupiterPrice()

    def get_price(self, symbol: str):
        if symbol == "SOL":
            price = self.raydium.get_price("SOL-USDC")
            if price:
                return price

        return self.jupiter.get_price(symbol)
