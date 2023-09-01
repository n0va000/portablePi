import guilib as gui
if gui.ask("Restart","Are you sure?"):
    from machine import reset
    machine.reset()