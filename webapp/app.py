from pathlib import Path

from flask import Flask, render_template
import pandas as pd

project_folder = Path(__file__).parent.parent
html_data = project_folder / 'data' / 'data.html'

app = Flask(__name__)


@app.route('/')
def index():
    with open(html_data, 'r', encoding='utf-8') as f:
        html_content = f.read()

    return render_template('page_data.html', html_data=html_content)


if __name__ == '__main__':
    app.run(port=5000)
