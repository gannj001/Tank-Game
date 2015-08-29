__author__ = 'John'

import sfml as sf

from Sandbox.Pathfinding.MoveBlocker import MoveBlocker
from SightPlayer import SightPlayer

game_size = sf.Vector2(800, 600)

# define game window
w, h = game_size
window = sf.RenderWindow(sf.VideoMode(w, h), "sight test")
window.vertical_synchronization = True

sb = MoveBlocker((200, 100))
sb.set_position((400, 300))
sp = SightPlayer(100, 100)

while window.is_open:
    # handle events
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()

    window.clear(sf.Color(50, 200, 50))

    sp.update([sb], sf.Mouse.get_position(window))
    window.draw(sb)
    window.draw(sp)
    window.draw(sp.los)

    window.display()
