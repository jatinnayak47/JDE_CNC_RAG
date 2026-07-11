import pandas as pd


class TicketLoader:

    @staticmethod
    def load(file_path: str):

        df = pd.read_excel(file_path)

        tickets = []

        for _, row in df.iterrows():

            ticket = {}

            for column in df.columns:

                value = row[column]

                ticket[column] = (
                    str(value)
                    if pd.notna(value)
                    else ""
                )

            tickets.append(ticket)

        return tickets