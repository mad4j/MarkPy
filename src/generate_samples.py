


from writedown.mdoc import MDoc
import writedown.renders.emphasys as em


def append_fragment(doc: MDoc, statements: str) -> None:

    d = MDoc(doc.page_width)
    exec(statements)

    doc.add_para("Python code")
    doc.add_code(statements, language="python")
    doc.add_para("Generated Markdown code")
    doc.add_code(d.get_doc(), language="markdown")
    doc.add_para("Rendered Markdown code")
    doc.append(d)

if __name__ == '__main__':

    doc = MDoc(80)
    doc.add_h1("MarkPy Samples")

    doc.add_h2("Heading samples")

    append_fragment(doc, """d.add_h1("Heading level 1")
d.add_h2("Heading level 2")
d.add_h3("Heading level 3")
d.add_h4("Heading level 4")
d.add_h5("Heading level 5")
d.add_h6("Heading level 6")
""")

    doc.add_ruler()

    doc.add_h2("Emphasys samples")
    append_fragment(doc, """d.add_para(em.bold("bold"))
d.add_para(em.italic("italic"))
d.add_para(em.code("code"))
d.add_para(em.highlight("highlight"))
""")

    doc.add_ruler()

    text = "This is an sample section text."

    doc.add_h2("Sections samples")
    append_fragment(doc, """d.add_para(text)
d.add_quote(text)
d.add_code(text)
""")

    doc.add_ruler()

    doc.add_h2("Lists samples")
    
    doc.add_h3("Ordered lists samples")
    append_fragment(doc, """
d.add_ol('One. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ol('Two. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ol('Three. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
""")
    
    doc.add_h3("Unordered lists samples")
    append_fragment(doc, """
d.add_ul('One. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ul('Two. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ul('Three. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
""")

    doc.add_h3("Definition lists samples")
    append_fragment(doc, """
d.add_dl('One.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_dl('Two.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_dl('Three.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
""")

    doc.add_ruler()

f = open("SAMPLES.md", "w")
f.write(doc.get_doc())
f.close()
