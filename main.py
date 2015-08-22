__author__ = 'John'

import sfml as sf

from Tank import TankBody
from Turret import TankTurret
from HUDParts import StatTracker
from Game import Game
from Destroyables import StationaryTarget


# define constants
game_size = sf.Vector2(800, 600)

# define game window
w, h = game_size
window = sf.RenderWindow(sf.VideoMode(w, h), "Tank-Game V1.0")
window.vertical_synchronization = True

# The tank should be created in the Game object
tank = TankBody(sf.Texture.from_file("res/RectTankDetailed.png"))
turret = TankTurret(sf.Texture.from_file("res/TankTurret.png"))

d = StationaryTarget(sf.Texture.from_file("res/Target.png"))
d.set_position((100, 500))

g = Game()
g.add_tank(tank)
g.add_target(d)
g.set_window(window)
g.set_keyboard(sf.Keyboard)
g.set_mouse(sf.Mouse)

s = StatTracker()
s.set_tracked_stat(turret.ready_to_fire)
s.set_position((700, 575))

turret.set_body(tank)
tank.set_turret(turret)

tank.position = game_size / 2

while window.is_open:
    # handle events
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()

    window.clear(sf.Color(50, 200, 50))
    if g.is_playing:
        g.update()
        s.update()

        g.draw_objects()

    window.display()
