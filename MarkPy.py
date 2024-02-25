
from md_utils import insert_breaks

class MDDocument:

    def __init__(self, page_width=40):
        self.doc = ""
        self.page_width = page_width
    
    def __add__(self, other):
        return self.addText(other)
    
    def __iadd__(self, other):
        return self.addText(other)
    
    def __str__(self):
        return self.doc


    def addHeading1(self, text: str):
        self.doc += "# " + text.strip() + "\n\n"

    def addUnderlinedHeading1(self, text: str, length = 0):
        text = text.strip()
        text = "# " + text + "\n"
        self.doc += text
        l = length if length > 0 else len(text)-1
        self.doc += "="*l + "\n\n"

    def addHeading2(self, text: str):
        self.doc += "## " + text.strip() + "\n\n"

    def addUnderlinedHeading2(self, text: str, length = 0):
        text = text.strip()
        text = "# " + text + "\n"
        self.doc += text
        l = length if length > 0 else len(text)-1
        self.doc += "-"*l + "\n\n"

    def addHeading3(self, text: str):
        self.doc += "### " + text.strip() + "\n\n"

    def addHeading4(self, text: str):
        self.doc += "#### " + text.strip() + "\n\n"

    def addHeading5(self, text: str):
        self.doc += "##### " + text.strip() + "\n\n"

    def addHeading6(self, text: str):
        self.doc += "###### " + text.strip() + "\n\n"

    def addParagraph(self, text: str):
        self.doc += text.strip() + "  \n\n"

    def addText(self, text: str):
        self.doc += text.strip() + "\n\n"

    def addBlock(self, text: str):
        text = text.lstrin()
        text = insert_breaks(text, self.page_width).splitlines()
        for line in text:
            self.doc += "> " + line + "\n"
        self.doc += "\n"
    
    def addTableHeader(self, *headers):
        self.doc += "|"
        for h in headers:
            self.doc += " " + h + " |"
        self.doc += "\n" + "|"
        for h in headers:
            self.doc += "-"*(len(h)+2) + "|"

    def addTableRow(self, *columns):
        self.doc += "\n" + "|"
        for h in columns:
            self.doc += " " + h.strip() + " |"    

    def addTableFooter(self):
        self.doc += "\n\n"


    def get(self):
        return self.doc
    

if __name__ == '__main__':

    d = MDDocument()

    d.addHeading1("Test Heading 1")
    d.addUnderlinedHeading1("Test Alternative Heading 1")

    d.addHeading2("Test Heading 2")
    d.addUnderlinedHeading2("Test Alternative Heading 2")

    d.addHeading3("Test Heading 3")
    d.addHeading4("Test Heading 4")
    d.addHeading5("Test Heading 5")
    d.addHeading6("Test Heading 6")

    d.addParagraph("This is a paragraph.")
    d.addParagraph("This is an other paragraph.")

    d.addBlock("This is a block of text.")

    d.addTableHeader("One", "Two", "Three")

    #d += "Simple text"

    print(d)