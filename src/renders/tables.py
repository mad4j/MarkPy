"""
"""


import re
from typing import List


def render_table_header(*headers) -> str:
    """
    """
    result = "|"
    for h in headers:
        result += h.replace(":", " ") + "|"
    result += "\n" + "|"
    for h in headers:
        result += re.sub("[^:]", "-", h) + "|"
    result += "\n"
    return result


def render_table_cell(text: str, width: int, align=0) -> str:
    """
    """
    text = text.strip()
    if align == 0:
        text = text.ljust(width, " ")
    elif align == 1:
        text = text.rjust(width, " ")
    else:
        text = text.center(width, " ")
    return text


def render_table_row(*columns: List[str], widths: List[int], aligns: List[int]) -> str:
    """
    """
    result = "|"
    counter = 0
    for h in columns:
        result += render_table_cell(
            h,
            widths[counter],
            aligns[counter]
        )
        result += "|"
        if counter < len(columns):
            counter += 1
    result += "\n"
    return result


def render_table_footer() -> str:
    """
    """
    return "\n"


def get_table_cell_align(header: str) -> int:
    """
    """
    # center-alignment case
    if header.startswith(":") and header.endswith(":"):
        return 2

    # right-alignment case
    if header.endswith(":"):
        return 1

    # left-alignment case
    if header.startswith(":"):
        return 0

    # otherwise left-alignment
    return 0