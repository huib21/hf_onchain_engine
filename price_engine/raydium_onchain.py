import base64
from typing import Optional
from .helius_rpc import HeliusRPC
import struct

class RaydiumOnChain:
    def __init__(self, rpc: HeliusRPC, pools: dict):
        self.rpc = rpc
        self.pools = pools

    def get_price(self, symbol: str) -> Optional[float]:
        if symbol not in self.pools:
            return None

        pool_pubkey = self.pools[symbol]

        # on-chain pool account fetch
        data = self.rpc.call(
            "getAccountInfo",
            [pool_pubkey, {"encoding": "base64"}]
        )

        try:
            raw = data["result"]["value"]["data"][0]
        except:
            return None

        decoded = base64.b64decode(raw)

        # Raydium pool layout: tokenA_reserve @ offset 80, tokenB_reserve @ offset 88
        # both are uint64 little endian
        token_a = struct.unpack_from("<Q", decoded, 80)[0]
        token_b = struct.unpack_from("<Q", decoded, 88)[0]

        if token_a == 0 or token_b == 0:
            return None

        price = token_b / token_a
        return price
