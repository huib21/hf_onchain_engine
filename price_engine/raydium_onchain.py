import base64
from price_engine.helius_rpc import HeliusRPC
from price_engine.config import RAYDIUM_POOLS

class RaydiumOnChain:
    def __init__(self):
        self.rpc = HeliusRPC()

    def get_price_from_pool(self, pool_pubkey: str):
        data = self.rpc.get_account(pool_pubkey)

        try:
            encoded = data["result"]["value"]["data"][0]
            decoded = base64.b64decode(encoded)

            export_price = int.from_bytes(decoded[200:208], "little") / 1e6
            return export_price

        except Exception:
            return None

    def get_price(self, symbol_pair: str):
        if symbol_pair not in RAYDIUM_POOLS:
            return None

        pub = RAYDIUM_POOLS[symbol_pair]
        return self.get_price_from_pool(pub)
