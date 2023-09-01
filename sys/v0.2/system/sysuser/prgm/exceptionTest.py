import guilib as gui
if gui.ask("what exception?","builtin","custom"):
    print(0/0)
else:
    raise Exception("Custom Exception")