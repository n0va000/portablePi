from clilib import cli
from dispobj import gp
import time
import machine
import sys
import os
import network
wlan = network.WLAN() #  network.WLAN(network.STA_IF)
wlan.active(True)
cli.printl("PPUTILS-INIT")
cli.printl("trying wlanD set")
try:
    import network
    import urequests
    cli.printl("setting wlanD")
    wlanDevice = network.WLAN(network.STA_IF)
    cli.printl("netWorks YES")
    netWorks = True
except:
    cli.printl("failed setting wlanD")
    cli.printl("netWorks NO")
    netWorks = False
ssid = "failed"
netpsd = "failed"
netWorks = False
try:
    cli.printl("imp items from EEPROM drv")
    from eeprom_i2c import EEPROM, T24C512
    cli.printl("setting eeprom")
    eep = EEPROM(gp.i2c, T24C512)
    eepromworks = True
except Exception as E:
    print("failed to load EEPROM")
    print(E)
    eepromworks = False
class eeprom:
    def __init__(self):
        self.eep = eep
        self.eepromworks = eepromworks
    def writeByte(self,pos,val):
        self.eep[pos] = val
    def readByte(self,pos):
        return self.eep[pos]
    def drive(self):
        return self.eep
    def verify(self):
        return self.eepromworks
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
    
    

def file_or_dir_exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError:
        return False
def dir_exists(filename):
    try:
        return (os.stat(filename)[0] & 0x4000) != 0
    except OSError:
        return False
        
def file_exists(filename):
    try:
        return (os.stat(filename)[0] & 0x4000) == 0
    except OSError:
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
