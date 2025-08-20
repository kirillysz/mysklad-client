from src.baseclient import BaseClient

from typing import List

class Assortment:
    def __init__(self, base: BaseClient):
        self.base = base
        self.prefix = "assortment"


    async def get_assortment(self) -> list[dict]:
        response = await self.base.request(
            endpoint=f"{self.prefix}", method="GET"
            )
        return response

    async def delete_assortment(self, items: list[dict]) -> dict:
        response = await self.base.request(
            endpoint=f"{self.prefix}/delete", 
            method="POST",
            data=items
        )
        return response
    
    