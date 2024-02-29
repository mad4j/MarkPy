"""
"""

__all__ = ["render_ul"]

from textwrap import fill

# valid unordered list placeholders
VALID_BULLETS = ["*", "-", "+"]

# Renders a single item of an unordered list.
def render_ul(text: str, placeholder="*", level=1, list_used_bullets=None, page_width=80) -> str:
    """
    Renders a single item of an unordered list.

    Args:
        text : str
            text to be displayed in list item
        placeholder : str
            unordered list bullet ["*", "-", "+"]
        level : int
            list nesting level (up to six levels)

    Returns:
        str : rendered list item as string

    Raises:
        ValueError : in case of invalid input argument
    """

    # check for default value
    if list_used_bullets is None:
        list_used_bullets = ["*"]

    # check 'level' value
    if level<=0 or level>6:
        raise ValueError(
            f"Given 'level' value ({level}) outside valid range [1..6]."
        )

    # store bullet used for this level for future coherence check
    if list_used_bullets[level] == "":
        list_used_bullets[level] = placeholder

    # veify incoherent usage of bullets by nesting levels
    if placeholder != list_used_bullets[level]:
        raise ValueError("")

    # check 'placeholder' value
    if placeholder not in VALID_BULLETS:
        raise ValueError(
            f"Given 'placeholder' value ('{placeholder}') is not valid "
                "(allowed values: {list_placeholders})."
        )


# TODO: verify item staring with Numeber-dot case

    # remove whithe spaces from 'text'
    result = text.strip()

    # item placeholder
    bullet = f"{placeholder} "

    # indentation spaces
    indent = "    "*(level-1)

    # extra spaces needed in subsequent indents
    extra_pad = " "*len(bullet)

    # render secion using placeholder and identation
    result = fill(
        text,
        width=page_width-len(indent),
        initial_indent=f"{indent}{placeholder} ",
        subsequent_indent=f"{indent}{extra_pad}"
    )

    # add an ending empty line
    result += "\n"

    # return rendered section
    return result
