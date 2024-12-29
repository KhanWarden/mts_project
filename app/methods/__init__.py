from .parser import fix_path, format_id
from .html import csv_page_to_html

__all__ = ['round_value',
           'fix_path',
           'format_id',
           'csv_page_to_html']


def round_value(value):
    if isinstance(value, float):
        return round(value, 2)
    return value
