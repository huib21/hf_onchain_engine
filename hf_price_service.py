from price_engine.helius_rpc import HeliusRPC
from price_engine.raydium_onchain import RaydiumOnChain
from price_engine.fallback_price import FallbackPrice
from price_engine.router import PriceRouter
from config import RPC_URL, RAYDIUM_POOLS, TOKENS
import time

class HFPriceService:
    def __init__(self):
        rpc = HeliusRPC(RPC_URL)
        raydium = RaydiumOnChain(rpc, RAYDIUM_POOLS)
        fallback = FallbackPrice()

        self.router = PriceRouter(
            raydium=raydium,
            fallback=fallback,
            raydium_pools=RAYDIUM_POOLS
        )

    def run(self):
        print("HF On-Chain Engine Running...\n")

        while True:
            prices = {}

            for t in TOKENS:
                p = self.router.get_price(t)
                if p is not None:
                    prices[t] = p

            print(prices)
            time.sleep(1)

if __name__ == "__main__":
    HFPriceService().run()
