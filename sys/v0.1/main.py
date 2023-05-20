import sys
import gc
sys.path.insert(1,"/prgm")
sys.path.insert(1,"/system")
sys.path.insert(1,"/system/lib")
sys.path.insert(1,"/system/drivers")

import guilib as gui
try:
    gui.clear()
    gui.cli.printl("Booting...")
    gui.cli.printl("imp os")
    import os
    gui.cli.printl("imp pputils")
    import pputils as psys
    gui.cli.printl("imp time")
    import time
    gui.cli.printl("collecting garbage")
    gc.collect()
    gui.cli.printl("Creating RBD")
    bdev = psys.RAMBlockDev(512, 50)
    gui.cli.printl("making RBD filesystem")
    os.VfsFat.mkfs(bdev)
    gui.cli.printl("mounting RBD")
    os.mount(bdev, '/rbd')
    time.sleep(1)
    gui.cli.printl("imp bprgm")
    import bprgm
    gui.cli.printl("collecting garbage")
    gc.collect()
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
