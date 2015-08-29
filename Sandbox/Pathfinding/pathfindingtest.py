import sfml as sf

from MoveBlocker import MoveBlocker
from PathfinderPlayer import PathfinderPlayer

game_size = sf.Vector2(800, 600)

# define game window
w, h = game_size
window = sf.RenderWindow(sf.VideoMode(w, h), "sight test")
window.vertical_synchronization = True

sb1 = MoveBlocker((200, 100))
sb1.set_position((400, 300))
sb2 = MoveBlocker((100, 100))
sb2.set_position((150, 250))
sb_list = [sb1, sb2]
pp = PathfinderPlayer(100, 100)

while window.is_open:
    # handle events
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()

    window.clear(sf.Color(50, 200, 50))

    pp.update(sb_list, sf.Mouse.get_position(window))
    for sb in sb_list:
        window.draw(sb)
    window.draw(pp)
    window.draw(pp.path)

    window.display()
