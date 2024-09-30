from decimal import Decimal

from src.report.dto import (
    CompanyDTO, CompanyGosDTO, CompanyTaxesInfoDTO, CompanyContactDTO, CompanyPhoneDTO,
    CompanyEmailDTO
)


class MapperKontur:

    @staticmethod
    def from_dict_to_company_info(base_info, taxes_info, gov_purchases) -> CompanyDTO:

        if base_info.get('IP'):
            name = base_info['IP']['fio']
            company_type = "IP"
        else:
            name = base_info['UL']['legalName']['full']
            company_type = "UL"

        okpo = base_info[company_type]['okpo']
        okato = base_info[company_type]['okato']
        okfs = base_info[company_type]['okfs']
        okogu = base_info[company_type]['okogu']
        okopf = base_info[company_type]['okopf']
        opf = base_info[company_type]['opf']
        oktmo = base_info[company_type]['oktmo']
        registration_date = base_info[company_type]['registrationDate']

        taxes_sum = Decimal(0)
        for item in taxes_info["taxes"]:
            for taxes_item in item["data"]:
                taxes_sum += Decimal(taxes_item["sum"])

        return CompanyDTO(
            name=name,
            opf=opf,
            okopf=okopf,
            oktmo=oktmo,
            okfs=okfs,
            okpo=okpo,
            okato=okato,
            okogu=okogu,
            registration_date=registration_date,
            gos=CompanyGosDTO(
                count=len(gov_purchases),
                sum=sum(
                    [
                        Decimal(item['contractPrice'])
                        for item in gov_purchases
                    ]
                )
            ),
            taxes=CompanyTaxesInfoDTO(
                data=taxes_info["taxes"],
                sum=taxes_sum
            ),
            contacts=CompanyContactDTO(
                contactPhones=CompanyPhoneDTO(count=base_info['contactPhones']['count']),
                contactEmails=CompanyEmailDTO(count=base_info['contactEmails']['count'])
            )
        )
