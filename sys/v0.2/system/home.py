if prc.sysprc != "enter_home":
    cli.printl("Unable to run this program!")
    sys.exit()
def main():
    from time import sleep
    cycle = 0
    maxCycles = 10
    from json import loads
    from ppsysutils import wlan
    netdata = {}
    cli.auto = True
    cli.printl("connecting")
    with open("/system/network.json","r") as f:
        netdata = loads(f.read())
    if netdata["active"]:
        wlan.active(True)
        if netdata["open"]:
            wlan.connect(netdata["ssid"],security = 0)
        else:
            wlan.connect(netdata["ssid"],netdata["pass"])
        while wlan.isconnected() == False:
                print('Waiting for connection...')
                cycle += 1
                sleep(1)
                if cycle == maxCycles:
                    cli.printl("timed out")
                    sleep(3)
                    break
    cli.auto = False
    cli.printl("preparing home")
    systemUser = users.user("user0")
    usersList = []
    selection = 0
    homeW = window("Home")
    msectionText = window.label("nill",12,13)
    l1Text = window.label("nill",0,21)
    l2Text = window.label("nill",0,30)
    l3Text = window.label("nill",0,38)
    l4Text = window.label("nill",0,46)
    # l5Text = window.label("nill",0,54)
    guideText = window.label("A. Back, B. Next, C. Page",0,56)
    msection = 0
    settings = os.listdir("/system/prgm")
    userAccount = users.user(users.cUser)
    userName = userAccount.getName()
    userDir = userAccount.getDir()
    sysAccount = users.user("sysUser")
    suserDir = sysAccount.getDir()
    programs = os.listdir(userDir+"/prgm")
    sprograms = os.listdir(suserDir+"/prgm")
    while 1:
        clear()
        msectionText.draw()
        if button.C.isPressed():
            msection += 1
            selection = 0
            msectionText.contents = "Nill"
        if msection == 0:
            msectionText.contents = "System"
            if button.A.isPressed():
                selection -= 1
            elif button.B.isPressed():
                selection += 1
            if selection == -1:
                selection = len(settings)-1
            elif selection == len(settings):
                selection = 0
            if button.E.isPressed():
                prc.prc = "/system/prgm/"+settings[selection]
                prc.prctype = 1 
                execfile("/system/prgm/"+settings[selection])
                prc.prctype = 0
                prc.prc = "None"
            l1Text.contents = "selected setting:"
            l2Text.contents = settings[selection].split(".")[0]
            l1Text.draw()
            l2Text.draw()
        elif msection == 1:
            msectionText.contents = "Log out."
            l1Text.contents = "Would you like to log out?"
            l2Text.contents = "you are: "+userName
            l3Text.contents = "E. Yes"
            l4Text.contents = "C. No"
            l1Text.draw()
            l2Text.draw()
            l3Text.draw()
            l4Text.draw()
            if button.E.isPressed():
                sys.exit()
        elif msection == 2:
            msectionText.contents = "Programs"
            if not len(programs) == 0:
                if button.A.isPressed():
                    selection -= 1
                elif button.B.isPressed():
                    selection += 1
                if selection == -1:
                    selection = len(programs)-1
                elif selection == len(programs):
                    selection = 0
                if button.E.isPressed():
                    try:
                        prc.prc = userDir+"/prgm/"+programs[selection]
                        prc.type = 2
                        execfile(userDir+"/prgm/"+programs[selection])
                        prc.type = 0
                        prc.prc = "None"
                    except Exception as E:
                        cli.auto = True
                        cli.printl(str(prc.type))
                        cli.printl(prc.prc)
                        prc.type = -1
                        cli.printl("Exception:")
                        cli.printl(str(E))
                        cli.printl("Program crashed!, press A")
                        while not button.A.isPressed():
                            pass
                l1Text.contents = "selected program:"
                l2Text.contents = programs[selection].split(".")[0]
                l1Text.draw()
                l2Text.draw()
            else:
                l1Text.contents = "no programs!"
                l1Text.draw()
        elif msection == 3:
            msectionText.contents = "System Programs"
            if not len(sprograms) == 0:
                if button.A.isPressed():
                    selection -= 1
                elif button.B.isPressed():
                    selection += 1
                if selection == -1:
                    selection = len(sprograms)-1
                elif selection == len(sprograms):
                    selection = 0
                if button.E.isPressed():
                    try:
                        prc.prc = userDir+"/prgm/"+sprograms[selection]
                        prc.type = 3
                        execfile(suserDir+"/prgm/"+sprograms[selection])
                        prc.type = 0
                        prc.prc = "None"
                    except Exception as E:
                        cli.auto = True
                        cli.printl(str(prc.type))
                        cli.printl(prc.prc)
                        prc.type = -1
                        cli.printl("Exception:")
                        cli.printl(str(E))
                        cli.printl("Program crashed!, press A")
                        while not button.A.isPressed():
                            pass
                        cli.auto = False
                l1Text.contents = "selected program:"
                l2Text.contents = sprograms[selection].split(".")[0]
                l1Text.draw()
                l2Text.draw()
            else:
                l1Text.contents = "no programs!"
                l1Text.draw()
        elif msection == 4:
            msection = 0
        drawLine(0,21,128,21)
        drawLine(8,21,8,13)
        guideText.draw()
        homeW.draw()
prc.sysprc = "home"
main()
