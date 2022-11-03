from typing import BinaryIO
import PyPDF2


def extract_pdf_data(file: BinaryIO) -> list[str]:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    return page.extractText().split("\n")


def extract_cost(data: list[str]) -> str | None:
    try:
        title_index = data.index("Total a Pagar")

        value = data[title_index + 1]
        value = value.replace("Vencimento", "")
        return value

    except Exception as err:
        print(err)
        return None


def extract_bill_month(data: list[str]) -> str | None:
    try:
        title_index = data.index("Conta Mês")

        month = data[title_index + 1]
        month = month.split("NOTA FISCAL")[0]
        return month

    except Exception as err:
        print(err)
        return None
