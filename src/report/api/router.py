from fastapi import APIRouter

from src.report.api.schema import GetCompanyInfoByInn
from src.report.dto import CompanyDTO
from src.report.service import ServiceReport
from src.service.client.httpx import AsyncHTTPXClient
from src.service.kontur.client import AsyncServiceKontur

report = APIRouter(prefix='/report', tags=['Отчет'])


@report.post('/get-company-info-by-inn', response_model=CompanyDTO)
async def get_compony_info_by_inn(schema: GetCompanyInfoByInn):
    kontur_client = AsyncServiceKontur(AsyncHTTPXClient())

    service = ServiceReport(kontur_client)
    return await service.get_compony_info_by_inn(schema.inn)

