lineTxt = []
from dispobj import display
class cli:
    auto = True
    def printl(text):
        text = str(text)
        print(text)
        '''prints text in cli'''
        def printInOrder():
            display.set_pen(0)
            display.clear()
            display.set_pen(15)
            for Txt in range(len(lineTxt)):
                display.text(str(lineTxt[Txt]), 0, Txt*8, 9999, 1)
            if cli.auto:
                display.update()
        if len(lineTxt)==8:
            del lineTxt[0]
        lineTxt.append(text)
        printInOrder()
    def clear():
        '''clears cli'''
        lineTxt = []
    def onDisp():
        '''get whats on display'''
        return lineTxt