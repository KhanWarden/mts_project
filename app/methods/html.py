import pandas as pd
from pathlib import Path

project_folder = Path(__file__).parent.parent.parent
csv_file = project_folder / 'data' / 'data.csv'
html_path = project_folder / 'data' / 'data.html'


async def csv_to_html(page: int):
    start_page = page * 5
    end_page = start_page + 5
    try:
        page_data = pd.read_csv(csv_file).iloc[start_page:end_page]
        html_content = page_data.to_html(index=False)
        with open(html_path, 'w') as f:
            f.write(html_content)
    except Exception as e:
        print(e)
