import re


def fix_path(path: str) -> str:
    return re.sub(r'[\\/]', r'//', path)
