from app.ingestion.loaders.base_loader import BaseLoader


class TxtLoader(BaseLoader):

    def load(self, file_path: str):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()