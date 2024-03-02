"""
"""

__all__ = ["render_hn", "render_uhn", "render_ruler"]


def render_hn(text: str, level=1) -> str:
    """Render a generic Heading.
    """
    return f"{'#'*level} {text.strip()}\n\n"


def render_uhn(text: str, level="=") -> str:
    """Render a generic Heading using userlined syntax.
    """
    return f"{text.strip()}\n{level*len(text)}\n\n"


def render_ruler(length=15) -> str:
    """Render an horizontal ruler separator.
    """
    return f"\n{'-'*length}\n\n"
