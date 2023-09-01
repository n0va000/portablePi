from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
gp = GfxPack()
display = gp.display
WIDTH, HEIGHT = display.get_bounds()
display.set_font("bitmap8")
def setFont(font="bitmap8"):
    display.set_font(font)