"""Easy Markdown document generation
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file

import re
from textwrap import fill


class MdDoc:
    """Class for easily generate pretty-readable Markdown documents.
    """

    def __init__(self, page_width=80) -> None:
        self.doc = ""
        self.page_width = page_width
        self.cell_widths = []
        self.cell_aligns = []
        self.list_used_bullets = ["", "", "", "", "", ""]

    def __add__(self, other):
        return self.add_text(other)

    def __iadd__(self, other):
        return self.add_text(other)

    def __str__(self):
        return self.doc

    def __render_hn(self, text: str, level=1) -> str:
        """Render a generic Heading.
        """
        return f"{'#'*level} {text.strip()}\n\n"

    def __render_uhn(self, text: str, level="=") -> str:
        """Render a generic Heading using userlined syntax.
        """
        return f"{text.strip()}\n{level*len(text)}\n\n"

    def __render_ruler(self, length=15) -> str:
        """
        """
        return f"\n{'-'*length}\n\n"

    def __render_text(self, text: str, trailer="\n\n") -> str:
        """
        """
        result = text.lstrip()
        result = fill(
            text,
            width=self.page_width,
        )
        result += trailer
        return result

    def __render_quote(self, text: str, trailer="\n\n") -> str:
        """
        """
        result = text.lstrip()
        result = fill(
            text,
            width=self.page_width,
            initial_indent="> ",
            subsequent_indent="> "
        )
        result += trailer
        return result



    # Renders a single item of an unordered list.
    def __render_ul(self, text: str, placeholder="*", level=1) -> str:
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
        # valid unordered list placeholders
        list_placeholders = ["*", "-", "+"]

        # check 'level' value
        if level<=0 or level>6:
            raise ValueError(
                f"Given 'level' value ({level}) outside valid range [1..6]."
            )

        # store bullet used for this level for future coherence check
        if self.list_used_bullets[level] == "":
            self.list_used_bullets[level] = placeholder

        # veify incoherent usage of bullets by nesting levels
        if placeholder != self.list_used_bullets[level]:
            raise ValueError("")

        # check 'placeholder' value
        if placeholder not in list_placeholders:
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
            width=self.page_width-len(indent),
            initial_indent=f"{indent}{placeholder} ",
            subsequent_indent=f"{indent}{extra_pad}"
        )

        # add an ending empty line
        result += "\n"

        # return rendered section
        return result

    def __render_table_header(self, *headers) -> str:
        """
        """
        self.cell_widths = list(map(len, headers))
        self.cell_aligns = list(map(self.__get_table_cell_align, headers))
        result = "|"
        for h in headers:
            result += h.replace(":", " ") + "|"
        result += "\n" + "|"
        for h in headers:
            result += re.sub("[^:]", "-", h) + "|"
        result += "\n"
        return result

    def __render_table_cell(self, text: str, width: int, align=0) -> str:
        """
        """
        text = text.strip()
        if align == 0:
            text = text.ljust(width, " ")
        elif align == 1:
            text = text.rjust(width, " ")
        else:
            text = text.center(width, " ")
        return text

    def __render_table_row(self, *columns) -> str:
        """
        """
        result = "|"
        counter = 0
        for h in columns:
            result += self.__render_table_cell(
                h,
                self.cell_widths[counter],
                self.cell_aligns[counter]
            )
            result += "|"
            if counter < len(columns):
                counter += 1
        result += "\n"
        return result

    def __render_table_footer(self) -> str:
        """
        """
        return "\n"

    def __get_table_cell_align(self, header: str) -> int:
        """
        """
        # center-alignment case
        if header.startswith(":") and header.endswith(":"):
            return 2

        # right-alignment case
        if header.endswith(":"):
            return 1

        # left-alignment case
        if header.startswith(":"):
            return 0

        # otherwise left-alignment
        return 0

    def add_h1(self, text: str) -> None:
        """Append a H1 heading to current document.
        """
        self.doc += self.__render_hn(text, level=1)

    def add_uh1(self, text: str) -> None:
        """Append a H1 heading to current document using underlined syntax.
        """
        self.doc += self.__render_uhn(text, level="=")

    def add_h2(self, text: str) -> None:
        """Append a H2 heading to current document.
        """
        self.doc += self.__render_hn(text, level=2)

    def add_uh2(self, text: str) -> None:
        """Append a H2 heading to current document using underlined syntax.
        """
        self.doc += self.__render_uhn(text, level="-")

    def add_h3(self, text: str) -> None:
        """Append a H3 heading to current document.
        """
        self.doc += self.__render_hn(text, level=3)

    def add_h4(self, text: str) -> None:
        """Append a H4 heading to current document.
        """
        self.doc += self.__render_hn(text, level=4)

    def add_h5(self, text: str) -> None:
        """Append a H5 heading to current document.
        """
        self.doc += self.__render_hn(text, level=5)

    def add_h6(self, text: str) -> None:
        """Append a H6 heading to current document.
        """
        self.doc += self.__render_hn(text, level=6)

    def add_ruler(self) -> None:
        """Append an horizontal ruler.
        """
        self.doc += self.__render_ruler(self.page_width)

    def add_par(self, text: str) -> None:
        """Append a new paragraph of text.
        """
        self.doc += self.__render_text(text, "  \n\n")

    def add_text(self, text: str) -> None:
        """Append unformatted text.
        """
        self.doc += self.__render_text(text)

    def add_quote(self, text: str) -> None:
        """Append a new blockquote section.
        """
        self.doc += self.__render_quote(text)

    def add_ul(self, text: str, placeholder="*", level=1):
        """Append a bullet of un un-ordered list
        """
        self.doc += self.__render_ul(text, placeholder, level)

    def add_table_header(self, *headers) -> None:
        """Append a new table header.
        """
        # add rendered header
        self.doc += self.__render_table_header(*headers)

    def add_table_row(self, *columns) -> None:
        """Append a new table row.
        """
        self.doc += self.__render_table_row(*columns)

    def add_table_footer(self) -> None:
        """Append a table trailer.
        """
        # add rendered footer
        self.doc += self.__render_table_footer()
        # reset internal table state
        self.cell_widths = []
        self.cell_aligns = []

    def get_doc(self) -> str:
        """Return the document as an str object.
        """
        # return interal document representation
        return self.doc


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

if __name__ == '__main__':

    d = MdDoc(25)

    d.add_h1("Test Heading 1")
    d.add_uh1("Test Alternative Heading 1")

    d.add_h2("Test Heading 2")
    d.add_uh2("Test Alternative Heading 2")

    d.add_h3("Test Heading 3")
    d.add_h4("Test Heading 4")
    d.add_h5("Test Heading 5")
    d.add_h6("Test Heading 6")

    d.add_par("This is a paragraph.")
    d.add_par("This is an other paragraph.")

    d.add_quote(
        "This is a silly block of text.\n"
        "To better work with Markdown files "
        "it should be useful to define a page width."
    )

    d.add_table_header(":One    ", ":Two   :", "Three    :")
    d.add_table_row("one", "two", "three")
    d.add_table_row("uno", "due", "tre")
    d.add_table_footer()

    d.add_ruler()

    d.add_ul("One")
    d.add_ul("Two")
    d.add_ul("This is a long list item. It is needed to wrap in more lines of text.")
    d.add_ul("Other item", level=2)
    d.add_ul("A longer other item", level=2)
    d.add_ul("An other item", level=2)
    d.add_ul("Three")

#   d += "Simple text"

    print(d)

#    d.add_ul("prova", level=20)
