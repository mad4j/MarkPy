"""
MarkPy - Easy Markdown document generator.

"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


from typing import List

from renders.lists import render_ul
from renders.headings import render_hn, render_uhn, render_ruler
from renders.tables import render_table_header, render_table_row, render_table_footer, get_table_cell_align
from renders.sections import render_para, render_quote

class MdDoc:

    """Class for easily generate pretty-readable Markdown documents.
    """

    def __init__(self, page_width=80) -> None:
        self.doc = ""
        self.page_width = page_width
        self.cell_widths = []
        self.cell_aligns = []
        self.list_used_bullets = ["", "", "", "", "", ""]

    def __str__(self):
        return self.doc


#   Headers and rulers
#   ------------------

    def add_h1(self, text: str) -> None:
        """Append a H1 heading to current document.
        """
        self.doc += render_hn(text, level=1)

    def add_uh1(self, text: str) -> None:
        """Append a H1 heading to current document using underlined syntax.
        """
        self.doc += render_uhn(text, level="=")

    def add_h2(self, text: str) -> None:
        """Append a H2 heading to current document.
        """
        self.doc += render_hn(text, level=2)

    def add_uh2(self, text: str) -> None:
        """Append a H2 heading to current document using underlined syntax.
        """
        self.doc += render_uhn(text, level="-")

    def add_h3(self, text: str) -> None:
        """Append a H3 heading to current document.
        """
        self.doc += render_hn(text, level=3)

    def add_h4(self, text: str) -> None:
        """Append a H4 heading to current document.
        """
        self.doc += render_hn(text, level=4)

    def add_h5(self, text: str) -> None:
        """Append a H5 heading to current document.
        """
        self.doc += render_hn(text, level=5)

    def add_h6(self, text: str) -> None:
        """Append a H6 heading to current document.
        """
        self.doc += render_hn(text, level=6)

    def add_ruler(self) -> None:
        """Append an horizontal ruler.
        """
        self.doc += render_ruler(self.page_width)



#   Sections
#   --------
        
    def add_para(self, text: str) -> None:
        """Append a new paragraph of text.
        """
        self.doc += render_para(text, page_width=self.page_width, trailer="  \n\n")

    def add_simple(self, text: str) -> None:
        """Append unformatted text.
        """
        self.doc += render_para(text, page_width=self.page_width)

    def add_quote(self, text: str) -> None:
        """Append a new blockquote section.
        """
        self.doc += render_quote(text, self.page_width)



#   Bullet lists
#   ------------

    def add_ul(self, text: str, placeholder="*", level=1):
        """Append a bullet of un un-ordered list
        """
        self.doc += render_ul(text, placeholder, level,
                              self.list_used_bullets,
                              self.page_width)


#   Tables
#   ------

    def add_table_header(self, *headers: List[str]) -> None:
        """Append a new table header.
        """

        # update interal state
        self.cell_widths = list(map(len, headers))
        self.cell_aligns = list(map(get_table_cell_align, headers))

        # add rendered header
        self.doc += render_table_header(*headers)


    def add_table_row(self, *columns) -> None:
        """Append a new table row.
        """
        self.doc += render_table_row(
            *columns, 
            widths=self.cell_widths,
            aligns=self.cell_aligns
        )

    def add_table_footer(self) -> None:
        """Append a table trailer.
        """
        # add rendered footer
        self.doc += render_table_footer()
        # reset internal table state
        self.cell_widths = []
        self.cell_aligns = []


    def get_doc(self) -> str:
        """Return the document as an str object.
        """
        # return interal document representation
        return self.doc


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

    d.add_para("This is a paragraph.")
    d.add_para("This is an other paragraph.")

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

    print(d)

#    d.add_ul("prova", level=20)
