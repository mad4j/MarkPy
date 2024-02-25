"""Easy Markdown document generation
"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file

from textwrap import fill


class MdDoc:
    """
    """
    def __init__(self, page_width=40) -> None:
        self.doc = ""
        self.page_width = page_width
        self.cell_widths = []
        self.cell_aligns = []

    def __add__(self, other):
        return self.add_text(other)

    def __iadd__(self, other):
        return self.add_text(other)

    def __str__(self):
        return self.doc

    def __render_hn(self, text: str, level=1) -> str:
        """
        """
        result = "#"*level + " " + text.strip() + "\n\n"
        return result
    
    def __render_uhn(self, text: str, level="=", length=0) -> str:
        """
        """
        result = text.strip()
        result = "# " + result + "\n"
        counter = length if length > 0 else len(result)-1
        result += level*counter + "\n\n"
        return result

    def add_h1(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=1)

    def add_uh1(self, text: str, length=0) -> None:
        """
        """
        self.doc += self.__render_uhn(text, "=", length)

    def add_h2(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=2)

    def add_uh2(self, text: str, length=0) -> None:
        """
        """
        self.doc += self.__render_uhn(text, "-", length)

    def add_h3(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=3)

    def add_h4(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=4)

    def add_h5(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=5)

    def add_h6(self, text: str) -> None:
        """
        """
        self.doc += self.__render_hn(text, level=6)

    def add_ruler(self):
        self.doc += "--- \n\n"
        return self

    def add_par(self, text: str):
        text = text.lstrip()
        text = fill(
            text,
            width=self.page_width,
        )
        self.doc += text + "  \n\n"
        return self

    def add_text(self, text: str):
        text = text.lstrip()
        text = fill(
            text,
            width=self.page_width,
        )
        self.doc += text + "\n\n"
        return self

    def add_block(self, text: str):
        text = text.lstrip()
        text = fill(
            text,
            width=self.page_width,
            initial_indent="> ",
            subsequent_indent="> "
        )
        self.doc += text + "\n\n"
        return self

    def add_table_header(self, *headers):
        self.doc += "|"
        for h in headers:
            self.doc += " " + h + " |"
        self.doc += "\n" + "|"
        for h in headers:
            self.doc += "-"*(len(h)+2) + "|"
        self.cell_widths = list(map(lambda x: len(x)+2, headers))
        return self

    def add_table_row(self, *columns):
        self.doc += "\n" + "|"
        for h in columns:
            self.doc += " " + h.strip() + " |"
        return self

    def add_table_footer(self):
        self.doc += "\n\n"
        self.cell_widths = []
        return self

    def get(self) -> str:
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

    d.add_par("This is a paragraph.")
    d.add_par("This is an other paragraph.")

    d.add_block(
        "This is a silly block of text.\n"
        "To better work with Markdown files "
        "it should be useful to define a page width."
    )

    d.add_table_header("One", "Two", "Three")

#   d += "Simple text"

    print(d)
