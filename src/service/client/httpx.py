from typing import Optional, Dict, Any

from fastapi import HTTPException, status
from httpx import AsyncClient, ConnectTimeout, HTTPStatusError, RequestError


class AsyncHTTPXClient:

    def __init__(self):
        self._client = AsyncClient(timeout=10)

    async def send(
        self,
        url: str,
        method: str = "GET",
        body: Optional[Any] = None,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
    ):
        try:
            response = await self._client.request(
                method, url, data=data, json=body, params=params, headers=headers
            )
            response.raise_for_status()
            return response.json()
        except ConnectTimeout:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable")
        except HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except RequestError:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
