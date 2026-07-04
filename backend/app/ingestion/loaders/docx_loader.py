from docx import Document

from app.ingestion.loaders.base_loader import BaseLoader


class DocxLoader(BaseLoader):

    def load(self, file_path: str):

        doc = Document(file_path)

        text = []

        for para in doc.paragraphs:
            text.append(para.text)

        return "\n".join(text)