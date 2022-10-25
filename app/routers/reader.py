from fastapi import APIRouter, Response, status, UploadFile
from pydantic import BaseModel

from helpers.extract_pdf_data import extract_pdf_data, extract_cost, extract_bill_month

router = APIRouter(prefix="/reader", tags=["reader"],
                   responses={404: {"message": "Rota não encontrada."}})


class ReaderResponse(BaseModel):
    message: str
    price: str | None = None
    month: str | None = None


@router.post("/", response_model=ReaderResponse)
async def root(response: Response, file: UploadFile):
    if file.content_type != "application/pdf":
        response.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        return {"message": "O arquivo enviado precisa ser um PDF."}

    data = extract_pdf_data(file.file)
    price = extract_cost(data)
    month = extract_bill_month(data)

    if price is None or month is None:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Não foi possível extrair os dados."}

    return {"message": "Dados extraídos com sucesso.", "price": price, "month": month}
