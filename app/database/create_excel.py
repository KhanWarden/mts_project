from pathlib import Path
import pandas as pd

project_folder = Path(__file__).parent.parent.parent
csv_file_path = project_folder / 'data' / 'data.csv'
excel_file_path = project_folder / 'data' / 'data.xlsx'


async def csv_to_excel():
    try:
        data = pd.read_csv(csv_file_path)
        data.to_excel(excel_file_path, index=False, engine='openpyxl')
    except Exception as e:
        print(e)
