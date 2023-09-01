def main():
    import userlib
    import guilib as gui
    import random
    import urequests
    import json
    if gui.ask("Where?","files","web"):
        temp = userlib.user(userlib.cUser)
        textfile = gui.file("pick text file", temp.getDir())
        del temp
        with open(textfile, "r") as f:
            text = f.read() + (" " * 32)
    else:
        if gui.ask("What?","URL","web shortcut"):
            url = gui.osk("URL?","abcdefghijklmnopqrstuvwxyz123456789-._~:/?#[]@!$&'()*+,;=")
            data = urequests.get(url)
            text = data.read()
    if gui.ask("fontsize?","normal","big"):
        font_size = 1
        chunk_size = 133
    else:
        font_size = 2
        chunk_size = 66
    chunks = [text[i * chunk_size : (i + 1) * chunk_size] for i in range(len(text) // chunk_size)]

    for i, chunk in enumerate(chunks):
        if chunk[0] == " ":
            chunk = chunk[1:]  # Remove the leading space
        
        gui.splash("-" +chunk + "-", fontsize=font_size)

if __name__ == "__main__":
    main()
