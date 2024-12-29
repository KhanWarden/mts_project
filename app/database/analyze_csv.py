import numpy as np
import pandas as pd
from .csv_parser import CSVParser


class AnalyzeCSV(CSVParser):
    def __init__(self):
        super().__init__()

    def get_top_n_max_values(self, column_name, n):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exist.")

        unique_values = set(self.data[column_name])
        unique_array = np.array(list(unique_values))
        top_values = np.sort(unique_array)[-n:][::-1]
        return top_values

    def get_top_n_min_values(self, column_name, n):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exist.")

        unique_values = set(self.data[column_name])
        unique_array = np.array(list(unique_values))
        top_values = np.sort(unique_array)[:n]
        return top_values

    def get_average_value(self, column_name):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exist.")

        column_data = self.data[column_name].to_numpy()
        average_value = np.mean(column_data)
        return average_value

    def calculate_correlation(self, column1, column2):
        if column1 not in self.data.columns or column2 not in self.data.columns:
            raise ValueError(f"'{column1}' or '{column2}' doesn't exist.")

        column1_values = self.data[column1].dropna().to_numpy()
        columns2_values = self.data[column2].dropna().to_numpy()

        correlation = np.corrcoef(column1_values, columns2_values)[0, 1]
        return correlation

    def calculate_productivity(self):
        average_performance_score = self.data['Performance_Score'].mean()
        average_stress_level = self.data['Stress_Level'].mean()

        productivity_coefficient = average_performance_score / average_stress_level

        return {
            "average_performance_score": average_performance_score,
            "average_stress_level": average_stress_level,
            "productivity_coefficient": productivity_coefficient
        }

    def best_student(self):
        best_student = self.data.sort_values(by=['Performance_Score', 'Stress_Level'], ascending=[False, True]).iloc[0]
        return best_student

    def most_engaged_student(self):
        most_engaged_student = self.data.sort_values(by=['Engagement_Level', 'Focus_Time'], ascending=[False, False]).iloc[0]
        return most_engaged_student

    def most_difficult_lesson(self):
        most_difficult_lesson = self.data.groupby('lesson_type')['stress_level'].mean().idxmax()
        return most_difficult_lesson
