from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
gp = GfxPack()
display = gp.display
class button:
    class A:
        def isDown():
            return gp.switch_pressed(SWITCH_A)
        def isPressed():
            if gp.switch_pressed(SWITCH_A):
                while gp.switch_pressed(SWITCH_A):
                    pass
                return 1
            else:
                return 0
    class B:
        def isDown():
            return gp.switch_pressed(SWITCH_B)
        def isPressed():
            if gp.switch_pressed(SWITCH_B):
                while gp.switch_pressed(SWITCH_B):
                    pass
                return 1
            else:
                return 0
    class C:
        def isDown():
            return gp.switch_pressed(SWITCH_C)
        def isPressed():
            if gp.switch_pressed(SWITCH_C):
                while gp.switch_pressed(SWITCH_C):
                    pass
                return 1
            else:
                return 0
    class D:
        def isDown():
            return gp.switch_pressed(SWITCH_D)
        def isPressed():
            if gp.switch_pressed(SWITCH_D):
                while gp.switch_pressed(SWITCH_D):
                    pass
                return 1
            else:
                return 0
    class E:
        def isDown():
            return gp.switch_pressed(SWITCH_E)
        def isPressed():
            if gp.switch_pressed(SWITCH_E):
                while gp.switch_pressed(SWITCH_E):
                    pass
                return 1
            else:
                return 0