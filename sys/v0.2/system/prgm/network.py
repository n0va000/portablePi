import guilib as gui
from ppsysutils import wlan
if __name__ == "__main__":
    wlan.active(True)
    maxCycles = 1
    selected = gui.menu("network settings","Manual connect","Scan connect","Exit")
    gui.msgBox(str(selected))
    if selected == 1:
        if gui.ask("Is the connection open?"):
            wlan.connect(gui.osk("ssid?"),security = 0)
            cycle = 0
            while wlan.isconnected() == False:
                print('Waiting for connection...')
                cycle += 1
                sleep(1)
                if cycle == maxCycles:
                    gui.msgBox("Timed out!")
                    pass
        else:
            wlan.connect(gui.osk("ssid?"),gui.osk("password?"))
            cycle = 0
            while wlan.isconnected() == False:
                print('Waiting for connection...')
                cycle += 1
                sleep(1)
                if cycle == maxCycles:
                    gui.msgBox("Timed out!")
                    pass
    elif selected == 2:
        networks = wlan.scan() # list with tupples with 6 fields ssid, bssid, channel, RSSI, security, hidden
        i=0
        networks.sort(key=lambda x:x[3],reverse=True) # sorted on RSSI (3)
        netdict = {}
        for w in networks:
            i+=1
            netdict[w[0].decode()] = str(w[4])+";"+str(w[5])
            gui.msgBox(str(netdict))
            