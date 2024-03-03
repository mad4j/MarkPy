"""
"""

from textwrap import fill



def plain(text: str, width=20) -> str:
    """Format a piece of plain text using provided 'width' as end-of-line limit.
    """
    return fill(text, width)


def render_para(text: str, page_width=80, trailer="\n\n") -> str:
    """
    Render a paragraph <p></p> section.
    To create paragraphs, use a blank line to separate one or more lines of text.
    """

    # remove unwanted white spaces
    result = text.lstrip()

    # text indentation a given page width
    result = fill(
        text,
        width=page_width,
    )

    ## add trailer (at least on empty line)
    result += trailer

    # return result value
    return result


def render_quote(text: str, page_width=80, trailer="\n\n") -> str:
    """
    """
    result = text.lstrip()
    result = fill(
        text,
        width=page_width,
        initial_indent="> ",
        subsequent_indent="  "
    )
    result += trailer
    return result

def render_code(text: str, language="", page_width=80) -> str:
    result = fill(
        text,
        width=page_width
    )

    result = f"```{language}\n{text}```\n\n"   

    return result


def render_line_break() -> str:
    """
    Render a line break.
    To create a line break or new line (<br>), end a line with two or more spaces, 
    and then type return.
    
    Returns:
        str: line break
    """
    return "  \n"
