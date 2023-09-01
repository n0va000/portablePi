from guilib import printAt, drawLine,update, drawImg
from dispobj import display, WIDTH, HEIGHT
class window:
    class label:
        def __init__(self,contents,x,y,size = 1):
            self.contents = contents
            self.x = x
            self.y = y
            self.size = size
        def draw(self):
            printAt(self.contents,self.x,self.y,self.size)
    def __init__(self,title,icon = False,iconp = ["111111111","10000001","10000001","111111111","10000001","10000001","10000001","11111111"]):
        self.title = title
        self.icon = icon
        if self.icon:
            self.iconp = iconp
    def draw(self):
        display.set_pen(0)
        display.rectangle
        if self.icon:
            printAt(self.title,13,3,1)
            drawImg(self.iconp,2,2)
        else:
            printAt(self.title,0,3,1)
        drawLine(0,0,WIDTH,0)
        drawLine(0,12,WIDTH,12)
        update()
