from aiohttp import ClientSession
from src.auth.authmanager import AuthManager

class BaseClient(AuthManager):
    def __init__(self, api_url: str, login: str, password: str):
        """
        Базовый класс для запросов по Ednpoint

        Args:
            api_url (str): API URL (может изменяться)
            token (str, optional): JWT токен. Defaults to "".
        """
        super().__init__(login=login, password=password)

        self.api_url = api_url
        self.session: ClientSession | None = None

    async def start(self):
        if not self.session:
            self.session = ClientSession()

            if not self.token:
                self.token = await self.get_token()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def request(self, endpoint: str, method: str = "GET", data: dict | None = None) -> Any:
        if not self.session:
            await self.start()

        url = f"{self.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        async with self.session.request(method=method.upper(), url=url, json=data, headers=headers) as resp:
            resp.raise_for_status()
            return await resp.json()