"""
MarkPy - Easy Markdown document generator.

Headings module.
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


from markpy.exceptions import InvalidArgumentException


# valid unordered list placeholders
VALID_RULER_CHARS = ["-", "*", "_"]

# valid unordered list placeholders
VALID_UNDERLINE_CHARS = ["=", "-"]


def render_hn(text: str, level=1) -> str:
    """Render a generic Heading.

    Something like:

    # A very important title

    Args:
        text (str): text to be diplayed as title
        level (int): heading importance level

    Returns:
        (str): rendered heading

    Raises:
        InvalidArgumentException: if not valid values provided as arguments

    """

    # verify for valid 'level' values
    if level<1 or level>6:
        raise InvalidArgumentException(
             f"Not a valid 'level' value ('{level}', use a value in range [1..6].")

    # remove unwanted white spaces
    text = text.strip()

    # return result value
    return f"{'#'*level} {text}\n\n"


def render_uhn(text: str, level=1) -> str:
    """
    Render a generic Heading using userlined syntax.

    Something like:

    A very important title
    ======================

    Args:
        text (str): text to be diplayed as title
        level (int): heading importance level

    Returns:
        (str): rendered heading

    Raises:
        InvalidArgumentException: if not valid values provided as arguments

    """
    # verify for valid 'level' values
    if level<1 or level>2:
        raise InvalidArgumentException(
            f"Not a valid 'level' value ('{level}', use a value in range [1..2].")

    # remove unwanted white spaces
    text = text.strip()

    # return result value
    return f"{text}\n{VALID_UNDERLINE_CHARS[level-1]*len(text)}\n\n"


def render_ruler(length: int = 3, separator: str = '-') -> (str | InvalidArgumentException):
    """
    Render an horizontal ruler separator.

    Something like:

    -----------------------------

    Args:
        length (int): lenght in chars of the horizontal ruler
        separator (str): char used as separator

    Returns:
        (str): rendered horizontal ruler

    Raises:
        InvalidArgumentException: if not valid values provided as arguments

    """

    # verify if 'separator' is a valid char
    if separator not in VALID_RULER_CHARS:
        raise InvalidArgumentException(
            f"Not a valid 'separator' char ('{separator}', use one from {VALID_RULER_CHARS})."
        )

    # verify for not negative 'lenght' values
    if length < 1:
        raise InvalidArgumentException(
            f"Not valid 'length' value ('{length}'), use positive values."
        )

    # minimum allowed length
    length = max(length, 3)

    # return result value
    return f"{separator*length}\n\n"
