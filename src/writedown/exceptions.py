"""
WriteDown - Easy Markdown document generator.

Exceptions module.
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file

class InvalidArgumentException(Exception):
    """Raised when the input value is not valid.
    """

class IncoherenceException(Exception):
    """Raised when the requested operation brings the document in an incoherent state.
    """
