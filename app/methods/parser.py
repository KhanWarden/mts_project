import re


def fix_path(path: str) -> str:
    return re.sub(r'[\\/]', r'//', path)


def format_id(num: int) -> str:
    return f"S{str(num).zfill(3)}"
