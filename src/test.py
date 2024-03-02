
from markpy.mdoc import MDoc


if __name__ == '__main__':

    d = MDoc(25)

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
