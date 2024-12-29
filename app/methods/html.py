import pandas as pd
from pathlib import Path

project_folder = Path(__file__).parent.parent.parent
csv_file = project_folder / 'data' / 'data.csv'
page_data_html_path = project_folder / 'data' / 'data.html'
data_html_path = project_folder / 'data' / 'stats.html'


async def csv_page_to_html(page: int):
    start_page = page * 5
    end_page = start_page + 5
    try:
        page_data = pd.read_csv(csv_file).iloc[start_page:end_page]
        html_content = page_data.to_html(index=False, classes="table table-bordered", border=0)
        with open(page_data_html_path, 'w') as f:
            f.write(html_content)
            f.close()
    except Exception as e:
        print(e)


async def data_to_html(string: str):
    try:
        with open(data_html_path, 'w') as f:
            f.write(string)
            f.close()
    except Exception as e:
        print(e)
