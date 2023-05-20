import time
try:
    import network
    import urequests
    wlanDevice = network.WLAN(network.STA_IF)
    netWorks = True
except:
    netWorks = False
try:
    import userdata
    ssid = userdata.netCred.ssid
    netpsd = userdata.netCred.psd
except:
    ssid = "failed"
    netpsd = "failed"    
def pholderImg(xsize,ysize):
    ''' place holder image generator'''
    empty = "0"*8
    full = "1"*8
    img = []
    for y in range(ysize):
        if (y % 2) == 0:
            img.append(empty)
        else:
            img.append(full)
    return img
def halt():
    '''halts'''
    while 1:
        pass
class wlan:
    state = False
    def setState(astate):
        ''' sets the hardwares state '''
        wlan.state = astate
        if netWorks:
            wlanDevice.active(astate)
            return True
        return False
    def connect(assid = ssid,anetpsd = netpsd):
        ''' trys connect to a wifi '''
        if netWorks:
            wlanDevice.connect(assid,anetpsd)
            return True
        return False
    def isConnected():
        ''' if its connected or not '''
        if netWorks:
            return wlanDevice.isconnected()
        return False
    def wget(url, asJson = True):
        ''' wifi get, optional arg to get as json (on by defualt) '''
        if netWorks:
            if wlan.isConnected():
                if asJson:
                    return urequests.get(url).json()
                else:
                    return urequests.get(url)
        return False
        
class RAMBlockDev:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num, buf):
        for i in range(len(buf)):
            buf[i] = self.data[block_num * self.block_size + i]

    def writeblocks(self, block_num, buf):
        for i in range(len(buf)):
            self.data[block_num * self.block_size + i] = buf[i]

    def ioctl(self, op, arg):
        if op == 4: # get number of blocks
            return len(self.data) // self.block_size
        if op == 5: # get block size
            return self.block_size