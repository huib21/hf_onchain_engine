from price_engine.helius_rpc import HeliusRPC
from price_engine.raydium_onchain import RaydiumOnChain
from price_engine.router import PriceRouter
from config import RPC_URL, RAYDIUM_POOLS, TOKENS
import time

class HFPriceService:
    def __init__(self):
        rpc = HeliusRPC(RPC_URL)
        raydium = RaydiumOnChain(rpc, RAYDIUM_POOLS)
        self.router = PriceRouter(raydium)

    def run(self):
        print("HF On-Chain Engine Running...\n")

        while True:
            out = {}
            for t in TOKENS:
                price = self.router.get_price(t)
                if price is not None:
                    out[t] = price

            print(out)
            time.sleep(1)

if __name__ == "__main__":
    HFPriceService().run()
