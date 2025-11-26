import base64
import struct

class RaydiumOnChain:
    def __init__(self, rpc, pools):
        self.rpc = rpc
        self.pools = pools

    def get_price(self, symbol: str):
        symbol = symbol.upper()

        if symbol not in self.pools:
            return None

        pool_pubkey = self.pools[symbol]

        # ultra short timeout → fallback kicks in quickly
        data = self.rpc.call(
            "getAccountInfo",
            [pool_pubkey, {"encoding": "base64"}],
            timeout=0.3
        )

        if (
            data is None
            or "result" not in data
            or data["result"] is None
            or data["result"]["value"] is None
            or "data" not in data["result"]["value"]
        ):
            return None

        try:
            encoded = data["result"]["value"]["data"][0]
            raw = base64.b64decode(encoded)

            BASE_DECIMALS = struct.unpack_from("<I", raw, 268)[0]
            QUOTE_DECIMALS = struct.unpack_from("<I", raw, 272)[0]
            PRICE = struct.unpack_from("<Q", raw, 280)[0]

            return PRICE / (10 ** (BASE_DECIMALS + QUOTE_DECIMALS))

        except:
            return None
