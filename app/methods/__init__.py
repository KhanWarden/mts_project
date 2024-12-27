from .parser import fix_path
from .html import csv_to_html

__all__ = ['round_value',
           'fix_path',
           'csv_to_html']


def round_value(value):
    if isinstance(value, float):
        return round(value, 2)
    return value
