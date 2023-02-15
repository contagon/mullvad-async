from typing import Optional

import aiohttp
from const import MULLVAD_API_ACCOUNT, MULLVAD_API_CONNECTED


class Mullvad:
    """
    An object that contains information extracted from Mullvad's API.
    """

    def __init__(self, session: aiohttp.ClientSession, user: Optional[str] = None):
        self._session = session
        self._user = user

    async def _request(self, url) -> dict:
        async with self._session.get(url) as resp:
            return await resp.json()

    async def account_status(self) -> dict:
        if self._user is None:
            raise MullvadAPIError(
                "User account not specified."
            )
        else:
            return await self._request(MULLVAD_API_ACCOUNT + self._user)

    async def is_connected(self) -> dict:
        return await self._request(MULLVAD_API_CONNECTED)


class MullvadAPIError(Exception):
    """Failed to fetch Mullvad API data."""
    pass