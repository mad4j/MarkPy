"""
MarkPy - Easy Markdown document generator.

Lists module.
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


import re
from textwrap import fill

from typing import List

from markpy.exceptions import IncoherenceException, InvalidArgumentException


# valid unordered list placeholders
LIST_VALID_MARKERS: List[str] = ['*', '-', '+']

# allowed number of nested lists
LIST_MAX_LEVEL: int = 6


def render_ol(
    text: str,
    level: int = 1,
    index: int = 1,
    page_width: int = 80
) -> str :

    """
    Renders a single item of an ordered list.
    
    To create an ordered list, add line items with numbers followed by periods. 
    The numbers don't have to be in numerical order, but the list should start 
    with the number one.

    Args:
        text : str
            text to be displayed in list item
        level : int
            list nesting level (up to six levels)
        index : int
            marker of list item
        page_width : int
            max list widht

    Returns:
        str : rendered list item as string

    Raises:
        None
    """

    # remove unwanted white spaces and end of lines
    result = text.strip()

    # item marker
    marker = f'{index:>3}.'

    # indentation spaces
    indent = '    '*(level-1)

    # extra spaces needed in subsequent indents
    extra_pad = ' '*len(marker)

    # render secion using bulltes and identation
    result = fill(
        text,
        width = page_width-len(indent),
        initial_indent = f'{indent}{marker} ',
        subsequent_indent = f'{indent}{extra_pad} '
    )

    # add an ending empty line
    result = f'{result}\n\n'

    # return rendered result
    return result


# Renders a single item of an unordered list.
def render_ul(
        text: str,
        bullet: str = '*',
        level: int = 1,
        list_used_bullets: List[str] | None =  None,
        page_width: int = 80
    ) -> str:

    """
    Renders a single item of an unordered list.
    
    To create an unordered list, add dashes (-), 
    asterisks (*), or plus signs (+) in front of line items. 
    Indent one or more items to create a nested list.

    Args:
        text : str
            text to be displayed in list item
        placeholder : str
            unordered list bullet ['*', '-', '+']
        level : int
            list nesting level (up to six levels)

    Returns:
        str : rendered list item as string

    Raises:
        InvalidArgumentException : in case of invalid input argument
        IncoherenceException : in case of usage of mixed styles
    """

    # check for default value
    if list_used_bullets is None:
        list_used_bullets = ['*']

    # check 'level' value
    if level<=0 or level>6:
        raise InvalidArgumentException(
            f'Given "level" value ({level}) outside valid range [1..6].'
        )

    # store bullet used for this level for future coherence check
    if list_used_bullets[level] == '':
        list_used_bullets[level] = bullet

    # veify incoherent usage of bullets by nesting levels
    if bullet != list_used_bullets[level]:
        raise IncoherenceException(
            f'Trying to use bullet "{bullet}" at level ({level})'
            'where previously used "{list_used_bullets[level]}".'
        )

    # check 'placeholder' value
    if bullet not in LIST_VALID_MARKERS:
        raise InvalidArgumentException(
            f'Given "placeholder" value ("{bullet}") is not valid '
            '(allowed values: {list_placeholders}).'
        )

    # remove unwanted white spaces and end of lines
    result = text.strip()

    # if you need to start an unordered list item with a number
    # followed by a period, you can use a backslash (\) to escape
    # the period.
    result = re.sub(r'(^\d+)\.', '\1\\.', result, 1)

    # list item placeholder
    bullet = f'{bullet}'

    # indentation spaces
    indent = '    '*(level-1)

    # extra spaces needed in subsequent indents
    extra_pad = ' '*len(bullet)

    # render secion using bulltes and identation
    result = fill(
        text,
        width = page_width-len(indent),
        initial_indent = f'{indent}{bullet} ',
        subsequent_indent = f'{indent}{extra_pad} '
    )

    # add an ending empty line
    result = f'{result}\n\n'

    # return rendered result
    return result


# Renders a single item of a definition list.
def render_dl(
        term: str,
        text: str,
        page_width: int = 80
    ) -> str:

    """
    Renders a single item of a definition list.
    
    Some Markdown processors allow you to create definition lists 
    of terms and their corresponding definitions. To create a definition 
    list, type the term on the first line. On the next line, type a 
    colon followed by a space and the definition.

    Args:
        term : str
            text to be displayed in list item
        text : str
            unordered list bullet ['*', '-', '+']
        page_width : int
            list nesting level (up to six levels)

    Returns:
        str : rendered list item as string

    Raises:
        None
    """

    # remove unwanted white spaces and end of lines
    term = term.strip()
    text = text.strip()

    # render 'term' using provided 'page_width'
    term = fill(
        term,
        width = page_width
    )

    # render 'text' using provided 'page_width'
    text = fill(
        text,
        width = page_width,
        initial_indent = ': ',
        subsequent_indent = '  '
    )

    # put together all parts
    result = f'{term}\n{text}\n\n'

    # return rendered result
    return result
