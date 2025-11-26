import time
from price_engine.router import PriceRouter

class HFPriceService:
    def __init__(self):
        self.router = PriceRouter()

    def run(self):
        print("HF Price Service running...")
        while True:
            sol = self.router.get_price("SOL")
            eth = self.router.get_price("ETH")
            bonk = self.router.get_price("BONK")

            print(f"SOL: {sol} | ETH: {eth} | BONK: {bonk}")
            time.sleep(2)

if __name__ == "__main__":
    HFPriceService().run()
