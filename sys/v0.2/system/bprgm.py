import userlib as users
from windowlib import window
from guilib import clear, drawLine
from buttonlib import button
      
if prc.sysprc != "enter_bprgm":
    cli.printl("Unable to run this program!")
    sys.exit()
def main():
    if button.A.isDown() and button.B.isDown() and button.D.isDown() and button.E.isDown():
        cli.printl("suser mode")
        while button.A.isDown() and button.B.isDown() and button.D.isDown() and button.E.isDown():
            pass
        users.cUser = "sysUser"
        execfile("/system/home.py")
    cli.printl("preparing logon")
    systemUser = users.user("user0")
    usersList = []
    for i in range(len(users.userJson)-1):
        usersList.append(users.userJson["user"+str(i)]["name"])
        cli.printl("fnd usr: "+usersList[i])
        if not psys.dir_exists(users.userJson["user"+str(i)]["dir"]): # makes sure user folder tree is okay
            cli.printl("u"+str(i)+": dir unfound, creating")
            os.mkdir(users.userJson["user"+str(i)]["dir"])
    selection = 0
    cli.auto = False # turns off cli
    logonW = window("Logon", True)
    userText = window.label("nill",12,13)
    theBigE = window.label("E-",14,29,3)
    loginText = window.label("Login",42,33,2)
    guideText = window.label("A. Back, B. Next",0,56)
    while 1:
        clear()
        if button.A.isPressed():
            selection -= 1
        elif button.B.isPressed():
            selection += 1
        if selection == -1:
            selection = len(usersList)-1
        elif selection == len(usersList):
            selection = 0
        if button.E.isPressed():
            users.cUser = "user"+str(selection)
            try:
                prc.sysprc = "enter_home"
                execfile("/system/home.py")
            except SystemExit:
                pass
        userText.contents = usersList[selection]
        userText.draw()
        drawLine(0,21,128,21)
        drawLine(8,21,8,13)
        theBigE.draw()
        loginText.draw()
        guideText.draw()
        logonW.draw()
prc.sysprc = "bprgm"
main()