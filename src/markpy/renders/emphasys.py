"""
MarkPy - Text emphasys module.
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


def bold(text: str) -> str:
    """
    Format a piece of text in bold.
    
    To bold text, add two asterisks or underscores before and after a word or phrase. 
    To bold the middle of a word for emphasis, add two asterisks without spaces around 
    the letters.
    
    Args:
        text (str): text to be emphatized
    
    Returns:
        str: rendered text
    """
    return f'**{text}**'


def italic(text: str) -> str:
    """
    Format a piece of text in italic.
    
    To italicize text, add one asterisk or underscore before and after a word or phrase. 
    To italicize the middle of a word for emphasis, add one asterisk without spaces around 
    the letters.
    
    Args:
        text (str): text to be emphatized
    
    Returns:
        str: rendered text
    """
    return f'*{text}*'


def code(text: str) -> str:
    """
    Format a piece of text as raw code.
    
    To denote a word or phrase as code, enclose it in backticks (`).
    
    Args:
        text (str): text to be emphatized
    
    Returns:
        str: rendered text
    """
    return f'`{text}`'


def highlight(text: str) -> str:
    """
    Format a piece using highlight feature.
    
    Some Markdown processors allow you to highlight text.
    To highlight words, use two equal signs (==) before and after the words.
    
    Args:
        text (str): text to be emphatized
    
    Returns:
        str: rendered text
    """
    return f'=={text}=='
