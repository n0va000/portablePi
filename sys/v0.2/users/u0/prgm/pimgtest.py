from time import sleep
import guilib as gui

# Assuming your display object is named 'display'
xs,ys,data = gui.pimgOpen("/users/u0/icon.pimg")
gui.drawBImg(data,0,0,xs,ys)
display.update()
sleep(5)