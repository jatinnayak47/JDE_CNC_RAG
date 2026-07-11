from pathlib import Path

from app.ingestion.loaders.docx_loader import (
    DocxLoader,
)

from app.ingestion.loaders.pdf_loader import (
    PdfLoader,
)

from app.ingestion.loaders.txt_loader import (
    TxtLoader,
)

from app.ingestion.loaders.excel_loader import (
    ExcelLoader,
)


class LoaderFactory:

    @staticmethod
    def get_loader(
        file_path: str
    ):

        extension = Path(
            file_path
        ).suffix.lower()

        if extension == ".pdf":
            return PdfLoader()

        if extension == ".docx":
            return DocxLoader()

        if extension == ".txt":
            return TxtLoader()

        if extension == ".xlsx":
            return ExcelLoader()

        if extension == ".xls":
            return ExcelLoader()

        raise ValueError(
            f"Unsupported file type: {extension}"
        )