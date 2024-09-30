import asyncio

from src.report.dto import CompanyDTO
from src.report.mapper import MapperKontur
from src.service.kontur.client import AsyncServiceKontur


class ServiceReport:

    def __init__(self, kontur_client: AsyncServiceKontur) -> None:
        self.kontur_client = kontur_client

    async def get_compony_info_by_inn(self, inn: str) -> CompanyDTO:

        base_info_task = self.kontur_client.get_base_info_by_inn(inn)
        taxes_info_task = self.kontur_client.get_taxes_info_by_inn(inn)
        gov_purchases_task = self.kontur_client.get_gov_purchases_of_customer_by_inn(inn)

        base_info, taxes_info, gov_purchases = await asyncio.gather(
            base_info_task, taxes_info_task, gov_purchases_task
        )

        return MapperKontur.from_dict_to_company_info(base_info, taxes_info, gov_purchases)
