if "prc" in locals(): 
    cli.printl("Unable to run boot program!")
    sys.exit()
import sys
sys.path.insert(1,"/prgm")
sys.path.insert(1,"/system")
sys.path.insert(1,"/system/lib")
sys.path.insert(1,"/system/drivers")
sys.path.insert(1,"/rbd")
from dispobj import display
from clilib import cli
try:
    display.set_pen(0)
    display.clear()
    display.set_pen(15)
    cli.printl("Booting...")
    cli.printl("imp gc")
    import gc
    cli.printl("imp os")
    import os
    cli.printl("imp pputils")
    import ppsysutils as psys
    cli.printl("imp time")
    import time
    cli.printl("collecting garbage")
    gc.collect()
    cli.printl("Creating RBD")
    bdev = psys.RAMBlockDev(512, 50)
    cli.printl("making RBD filesystem")
    os.VfsFat.mkfs(bdev)
    cli.printl("mounting RBD")
    os.mount(bdev, '/rbd')
    cli.printl("creating sysprc in RBD")
    with open('/rbd/prc.py', 'w') as f:
        f.write("sysprc = \"BOOTPRC\"\nprc = \"system\"\nsys = 0.2\nprctype = 0")
        pass
    import prc
    cli.printl("executing bprgm")
    try:
        prc.sysprc = "enter_bprgm"
        execfile("/system/bprgm.py")
    except SystemExit:
        prc.sysprc = "sysexit"
        cli.auto = True
        cli.printl("!!quit!! system halted")
        while 1:
            pass
    cli.printl("collecting garbage")
    gc.collect()
    cli.auto = True
    cli.printl("!!eoc!! system halted")  # end of code, should not reach here
    prc.sysprc = "eoc"
    while 1:
        pass
    
except Exception as e:
    cli.auto = True
    cli.printl("CRITICAL ERROR")
    cli.printl(str(e))
    print(e)
    while 1:
        pass