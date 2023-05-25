import guilib as gui
gui.splash("Welcome to the web homepage")
ans = gui.menu("what do you want to do?", "download app downloader","enter a url")
gui.msgBox(str(ans))
