
def insert_breaks(text: str, width=25):
    last_break = 0
    last_space = 0
    for i in range(len(text)):
        c = text[i:i+1]
        if c == "\n":
            last_break = i
        elif c.isspace():
            last_space = i
        else:
            if (i - last_break) > width:
                text = text[:last_space] + "\n" + text[last_space+1:]
                last_break = last_space
    return text

if __name__ == '__main__':
    text = "Questa è una prova di scrittura.\nDovrebbe essere possibile suddividere questa stringa in più parti."
    text = insert_breaks(text, 20)
    print(text)