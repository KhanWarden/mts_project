import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = load_data(file_path)

    def index_columns(self):
        self.data.set_index('Student_ID', inplace=True)

    def get_column(self, column_name):
        # получаем столбец по имени
        return self.data[column_name]

    def get_row(self, student_id):
        # получаем строку по Student_ID
        return self.data.loc[student_id]

    def filter_data(self, column_name, value):
        # фильтруем данные по значению в столбце
        return self.data[self.data[column_name] == value]

    def get_all_data(self):
        # возвращаем все данные
        return self.data

    def add_new_row(self, row_data):
        # добавляем новую строку в dataframe
        self.data = self.data.append(row_data, ignore_index=True)

    def save_data(self, file_path=None):
        # сохраняем dataframe обратно в csv
        if file_path is None:
            file_path = self.file_path
        self.data.to_csv(file_path)
