from pydantic import BaseModel, EmailStr, UUID4, field_validator
import re


class GetCompanyInfoByInn(BaseModel):
    fio_client: str
    email_client: EmailStr
    arbitrary_key: UUID4
    report_name: str
    inn: str

    @classmethod
    @field_validator('fio_client')
    def validate_fio_client(cls, v):
        if not v.strip():
            raise ValueError('ФИО клиента не может быть пустым')
        return v

    @classmethod
    @field_validator('report_name')
    def validate_report_name(cls, v):
        if not v.strip():
            raise ValueError('Название отчета не может быть пустым')
        return v

    @classmethod
    @field_validator('inn')
    def validate_inn(cls, v):
        if not re.fullmatch(r'\d{10}|\d{12}', v):
            raise ValueError('ИНН должен содержать 10 или 12 цифр')
        return v