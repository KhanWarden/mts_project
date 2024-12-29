from pathlib import Path
import pandas as pd

from app.methods import round_value

project_folder = Path(__file__).parent.parent.parent
csv_file = project_folder / 'data' / 'data.csv'


def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return None
    except Exception as e:
        raise e


class CSVParser:
    def __init__(self):
        self.file_path = csv_file
        self.data = load_data(csv_file)
        self.index_columns()

    def index_columns(self):
        self.data.set_index('Student_ID', inplace=True)

    def get_row(self, student_id):
        return self.data.loc[student_id]

    def get_formatted_row(self, student_id):
        row = self.get_row(student_id)
        result = ""
        for column, value in row.items():
            result += f"<b>{column}:</b> {round_value(value)}\n"
        return result

    def get_columns_names(self) -> tuple:
        return tuple(self.data.columns)

    def get_unique_column_values(self, column_name) -> set:
        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' doesn't exist.")
        return set(self.data[column_name])


def get_page(page: int):
    start_page = page * 5
    end_page = start_page + 5
    try:
        page_data = pd.read_csv(csv_file).iloc[start_page:end_page]
        formatted_data = ""
        for _, row in page_data.iterrows():
            for columnn, value in row.items():
                formatted_data += f"<b>{columnn}:</b> {round_value(value)}\n"
            formatted_data += "\n"
        return formatted_data
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
