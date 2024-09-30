from abc import ABC
from typing import Dict

from src.service.client.httpx import AsyncHTTPXClient


class BaseServiceKontur(ABC):

    # В проде убрать в .env
    API_TOKEN = "3208d29d15c507395db770d0e65f3711e40374df"
    API_URL = "https://focus-api.kontur.ru/api3"

    @staticmethod
    def _default_query_params():
        return {
            "key": "3208d29d15c507395db770d0e65f3711e40374df"
        }


class AsyncServiceKontur(BaseServiceKontur):

    def __init__(self, async_client: AsyncHTTPXClient) -> None:
        super().__init__()
        self.async_client = async_client

    async def get_base_info_by_inn(self, inn: str) -> Dict:
        """Получить базовую информацию о компании"""
        res = await self.async_client.send(
            url=self.API_URL + '/req',
            params={
                **self._default_query_params(),
                'inn': inn
            }
        )
        return res[0]

    async def get_taxes_info_by_inn(self, inn: str) -> Dict:
        """Получить информацию о налогах"""
        return await self.async_client.send(
            url=self.API_URL + '/taxes',
            params={
                **self._default_query_params(),
                'inn': inn
            }
        )

    async def get_gov_purchases_of_customer_by_inn(self, inn: str) -> Dict:
        """Получить информацию о гос закупках"""
        return await self.async_client.send(
            url=self.API_URL + '/govPurchasesOfCustomer',
            params={
                **self._default_query_params(),
                'inn': inn
            }
        )
