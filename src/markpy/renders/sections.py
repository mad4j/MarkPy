"""
"""

from textwrap import fill


def render_para(text: str, page_width=80, trailer="\n\n") -> str:
    """
    """
    result = text.lstrip()
    result = fill(
        text,
        width=page_width,
    )
    result += trailer
    return result

def render_quote(text: str, page_width=80, trailer="\n\n") -> str:
    """
    """
    result = text.lstrip()
    result = fill(
        text,
        width=page_width,
        initial_indent="> ",
        subsequent_indent="> "
    )
    result += trailer
    return result