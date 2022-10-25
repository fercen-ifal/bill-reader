from typing import BinaryIO
import PyPDF2


def extract_pdf_data(file: BinaryIO) -> list[str]:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    return page.extractText().split("\n")


def extract_cost(data: list[str]) -> str:
    title_index = data.index("Total a Pagar")

    if title_index == -1:
        return None

    value = data[title_index + 1]
    value = value.replace("Vencimento", "")
    return value


def extract_bill_month(data: list[str]) -> str:
    title_index = data.index("Conta Mês")

    if title_index == -1:
        return None

    month = data[title_index + 1]
    month = month.split("NOTA FISCAL")[0]
    return month
