from pathlib import Path

from flask import Flask, render_template, request, session, jsonify
import pandas as pd

project_folder = Path(__file__).parent.parent
html_data = project_folder / 'data' / 'data.html'

app = Flask(__name__)
app.secret_key = 'mts'


@app.route('/page')
def index():
    with open(html_data, 'r', encoding='utf-8') as f:
        html_content = f.read()

    return render_template('page_data.html', html_data=html_content)


@app.route('/values', methods=['GET', 'POST'])
def values():
    values_str = request.args.get("values", "")
    if values_str:
        values = [float(value.strip()) for value in values_str.split(',')]
    else:
        values = []
    return render_template("values.html", values=values)


if __name__ == '__main__':
    app.run(port=5000,
            debug=True)
