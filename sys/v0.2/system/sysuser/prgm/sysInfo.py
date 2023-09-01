def main():
    import guilib as gui
    import os
    from buttonlib import button
    import micropython
    import gc
    import time
    gc.collect()
    gui.clear()
    gui.printAt("Flash: "+str(os.statvfs("/")[0]/2)+"KB/2"+str(os.statvfs("/")[3]/2)+"KB Used",0,0,1)
    gui.printAt("Ramdsk: "+"8.0KB/"+str(os.statvfs("/rbd")[3]/2)+"KB Used",0,8,1)
    gui.printAt("Ram: "+"264KB/"+str(gc.mem_free()/1000)+"KB Free",0,16,1)
    gui.printAt("Board: "+sys.platform,0,24,1)
    gui.printAt("Press A to continue",0,56,1)
    gui.update()
    while not button.A.isPressed():
        pass
    gui.clear()
    gui.printAt("Mpyver: "+os.uname()[2],0,0,1)
    gui.printAt("Pyver: "+sys.version,0,8,1)
    gui.printAt("Press A to continue",0,56,1)
    gui.update()
    while not button.A.isPressed():
        pass
if __name__ == "__main__":
    main()