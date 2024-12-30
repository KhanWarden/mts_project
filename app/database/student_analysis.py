import pandas as pd
import numpy as np
from app.database import AnalyzeCSV


class StudentAnalysis(AnalyzeCSV):
    def __init__(self):
        super().__init__()

    def get_average_value(self, column_name):
        if column_name not in self.data.columns:
            raise ValueError(f"{column_name} doesn't exist.")

        column_data = self.data[column_name].to_numpy()
        average_value = np.mean(column_data)
        return average_value

    def calculate_correlation_of_student(self, column1, column2, student_id):
        if column1 not in self.data.columns or column2 not in self.data.columns:
            raise ValueError(f"'{column1}' or '{column2}' doesn't exist.")

        student_data = self.data[self.data["Student_ID"] == student_id]
        if student_data.empty():
            raise ValueError(f"Student '{student_id}' doesn't exist.")

        column1_values = student_data[column1].dropna().to_numpy()
        columns2_values = student_data[column2].dropna().to_numpy()

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

    def engagement_impact_on_skill_development(self):
        self.data['Normalized_Engagement'] = self.data['Engagement_Level'] / 10
        correlation = self.calculate_correlation('Normalized_Engagement', 'Skill_Development')
        return correlation
