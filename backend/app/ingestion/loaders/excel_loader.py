import pandas as pd

from app.ingestion.loaders.base_loader import (
    BaseLoader
)


class ExcelLoader(BaseLoader):

    def load(
        self,
        file_path: str
    ):

        df = pd.read_excel(
            file_path
        )

        incidents = []

        for _, row in df.iterrows():

            ticket_text = []

            for column in df.columns:

                value = row[column]

                if pd.notna(value):

                    ticket_text.append(
                        f"{column}: {value}"
                    )

            incidents.append(
                "\n".join(ticket_text)
            )

        return "\n\n".join(
            incidents
        )