from decimal import Decimal
from typing import List

from pydantic import BaseModel


class CompanyPhoneDTO(BaseModel):
    count: int


class CompanyEmailDTO(BaseModel):
    count: int


class CompanyContactDTO(BaseModel):
    contactPhones: CompanyPhoneDTO
    contactEmails: CompanyEmailDTO


class CompanyGosDTO(BaseModel):
    count: int
    sum: Decimal


class CompanyTaxesDetailInfoDTO(BaseModel):
    name: str
    sum: Decimal


class CompanyTaxesDTO(BaseModel):
    year: int
    data: List[CompanyTaxesDetailInfoDTO]


class CompanyTaxesInfoDTO(BaseModel):
    data: List[CompanyTaxesDTO]
    sum: Decimal


class CompanyDTO(BaseModel):
    name: str
    kpp: str | None
    okpo: str
    okato: str
    okfs: str
    okogu: str
    okopf: str
    opf: str
    oktmo: str
    registrationDate: str
    contacts: CompanyContactDTO
    taxes: CompanyTaxesInfoDTO
    gos: CompanyGosDTO

