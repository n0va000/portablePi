def main():
    from ppsysutils import eeprom
    import guilib as gui
    eeprom = eeprom()
    if eeprom.verify(): # checks if an eeprom is connected and working
        gui.splash("eeprom size: "+str(len(eeprom.drive())))
    else:
        gui.msgbox("no eeprom found!")
main()