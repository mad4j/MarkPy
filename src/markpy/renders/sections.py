"""
MarkPy - Text sections module.
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


from textwrap import fill

def render_plain(text: str, page_width: int = 20) -> str:
    """
    Format a piece of plain text using provided 'width' as end-of-line limit.
    
    Args:
        text (str): text to be emphatized
        width (int): page width
        
    Returns:
        str: rendered text
    """

    # remove unwanted spces and end-lines
    text = text.strip()

    # split using 'page_width' as limit
    result = fill(
        text,
        width = page_width
    )

    # return rendered text
    return result


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

def render_code(text: str, language: str = "text", page_width: int = 80) -> str:
    """
    Format a piece of text using fenced code formatting.
    
    Args:
        text (str): text to be emphatized
        width (int): page end-of-line limit
        
    Returns:
        str: rendered text
    """

    # use 'text' if syntax highlight language is not provided
    if language is None or language == '':
        language = 'text'

    # remove unwanted line endings
    text = text.strip()

    # escape backticks eventually contained in 'text'
    if '`' in text:
        text = f'`` {text} ``'

    # split lines at given 'page_with'
    result = fill(
        text,
        width=page_width
    )

    # add code fences
    result = f'```{language}\n{text}\n```\n\n'

    # return result value
    return result


def render_line_break() -> str:
    """
    Render a line break.
    To create a line break or new line (<br>), end a line with two or more spaces, 
    and then type return.
    
    Returns:
        str: rendered line break
    """
    return '  \n'
