import base64

from aiohttp import ClientSession

class AuthManager:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

        self.auth_url = "https://api.moysklad.ru/api/remap/1.2/security/token"
        self.token: str | None = None

    async def get_token(self) -> str:
        """
        Получение JWT токена по логину и паролю через Basic Auth (Base64).
        """
        credentials = f"{self.login}:{self.password}".encode("utf-8")
        encoded_credentials = base64.b64encode(credentials).decode("utf-8")

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip"
        }

        async with ClientSession() as session:
            async with session.post(url=self.auth_url, headers=headers) as resp:
                resp.raise_for_status()

                data = await resp.json()
                self.token = data.get("access_token")

                return self.token