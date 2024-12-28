import numpy as np
import pandas as pd
from .csv_parser import CSVParser


class AnalyzeCSV(CSVParser):
    def __init__(self):
        super().__init__()

    def get_top_n_max_values(self, column_name, n):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exists.")

        column_data = self.data[column_name].to_numpy()
        unique_values = set(self.data[column_name])
        unique_array = np.array(list(unique_values))
        top_values = np.sort(column_data)[-n:][::-1]
        return top_values

    def get_top_n_min_values(self, column_name, n):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exists.")

        column_data = self.data[column_name].to_numpy()
        unique_values = set(self.data[column_name])
        unique_array = np.array(list(unique_values))
        top_values = np.sort(column_data)[:n]
        return top_values

    def get_average_value(self, column_name):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exists.")

        column_data = self.data[column_name].to_numpy()
        average_value = np.mean(column_data)
        return average_value
