__author__ = 'John'

import sfml as sf

from Tank import TankBody
from Turret import TankTurret
from HUDParts import StatTracker


class Game:
    def __init__(self):
        self.tanks = []
        self.window = None
        self.HUDObjects = []

    def add_tank(self, tank):
        self.tanks.append(tank)

    def add_HUD_parts(self, HUDPart):
        self.HUDObjects.append(HUDPart)

    def set_window(self, window):
        self.window = window

    def draw_objects(self):
        for tank in self.tanks:
            self.window.draw(tank)
            for shell in tank.turret.shells:
                self.window.draw(shell)
            self.window.draw(tank.turret)

        for HUDPart in self.HUDObjects:
            HUDPart.update()


# define constants
game_size = sf.Vector2(800, 600)

# define game window
w, h = game_size
window = sf.RenderWindow(sf.VideoMode(w, h), "pySFML - Tank Test 6")
window.vertical_synchronization = True

tank = TankBody(sf.Texture.from_file("res/RectTankDetailed.png"))
turret = TankTurret(sf.Texture.from_file("res/TankTurret.png"))
g = Game()
g.add_tank(tank)
g.set_window(window)

s = StatTracker()
s.set_tracked_stat(turret.ready_to_fire)
s.set_position((750, 550))

turret.set_body(tank)
tank.set_turret(turret)

tank.position = game_size / 2

while window.is_open:
    # handle events
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
            # The keyboard should be passed into the tank.update() function, not altering the tank here.

    window.clear(sf.Color(50, 200, 50))

    tank.update(sf.Mouse, window, sf.Keyboard)
    s.update()

    g.draw_objects()

    window.display()
