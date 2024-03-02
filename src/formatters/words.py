"""
"""

__all__ = ["bold", "italic", "code", "highlight", "plain"]

from textwrap import fill


def bold(text: str) -> str:
    """Format a piece of text in bold.
    """
    return f"**{text}**"

def italic(text: str) -> str:
    """Format a piece of text in italic.
    """
    return f"*{text}*"

def code(text: str) -> str:
    """Format a piece of text as raw code.
    """
    return f"`{text}`"

def highlight(text: str) -> str:
    """Format a piece using highlight feature.
    """
    return f"=={text}=="

def plain(text: str, width=20) -> str:
    """Format a piece of plain text using provided 'width' as end-of-line limit.
    """
    return fill(text, width)
