from src.baseclient import BaseClient
from typing import List

class Assortment:
    def __init__(self, base: BaseClient):
        self.base = base
        self.prefix = "assortment"

    async def get_assortiment(self):
        response = await self.base.request(
            endpoint=f"{self.prefix}", method="GET"
            )
        return response
