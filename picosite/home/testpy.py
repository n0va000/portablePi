import guilib as gui
import random
try:
  gui.msgBox("This is python!")
  gui.msgBox(gui.osk("type something"))
  gui.msgBox("Alright, try guess a number from 1 to 10!")
  number = random.randint(1,10)
  while 1:
    picked = int(gui.osk("guess a number","0123456789"))
    if number == picked:
      gui.msgBox("You win!!")
      break
    elif picked > number:
      gui.msgBox("target number is smaller")
    elif number > picked:
      gui.msgBox("target number is bigger")
Except:
  gui.msgBox("Oh no an error occured in the demo")
