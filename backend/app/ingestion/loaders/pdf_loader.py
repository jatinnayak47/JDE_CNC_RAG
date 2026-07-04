import fitz

from app.ingestion.loaders.base_loader import BaseLoader


class PdfLoader(BaseLoader):

    def load(self, file_path: str):

        document = fitz.open(file_path)

        pages = []

        for page in document:
            pages.append(page.get_text())

        return "\n".join(pages)