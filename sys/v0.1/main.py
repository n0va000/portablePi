import sys
sys.path.insert(1,"/prgm")
sys.path.insert(1,"/system")
sys.path.insert(1,"/system/lib")
sys.path.insert(1,"/system/drivers")
import os
import pputils as psys
import guilib as gui
import time
try:
    gui.clear()
    gui.cli.printl("Booting...")
    gui.cli.printl("Creating RBD")
    bdev = psys.RAMBlockDev(512, 50)
    gui.cli.printl("making RBD filesystem")
    os.VfsFat.mkfs(bdev)
    gui.cli.printl("mounting RBD")
    os.mount(bdev, '/rbd')
    time.sleep(1)
    gui.cli.printl("imp bprgm")
    import bprgm
    gui.cli.printl("entering bprgm")
    bprgm.main()
    gui.cli.auto = True
    gui.cli.printl("!!eoc!!")  # end of code, should not reach here
    psys.halt()
    
except Exception as e:
    gui.cli.auto = True
    gui.cli.printl("CRITICAL ERROR")
    gui.cli.printl(str(e))
    print(e)
    psys.halt()