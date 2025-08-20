from aiohttp import ClientSession

class BaseClient:
    def __init__(self, api_url: str, token: str = ""):
        self.api_url = api_url
        self.token = token

        self.session: ClientSession | None = None

    async def start(self):
        if not self.session:
            self.session = ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def request(self, endpoint: str, method: str = "GET", data: dict = None):
        if not self.session:
            await self.start()

        url = f"{self.api_url}/api/{endpoint.lstrip('/')}"
        
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        async with self.session.request(method=method.upper(), url=url, json=data, headers=headers) as resp:
            text = await resp.text()
            if not resp.ok:
                raise Exception(f"Request failed {resp.status}: {text}")

            return await resp.json()
