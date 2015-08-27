__author__ = 'John'

import sfml as sf

from MenuScreen import MenuScreen

# define constants
game_size = sf.Vector2(800, 600)

# define game window
w, h = game_size
window = sf.RenderWindow(sf.VideoMode(w, h), "Tank-Game V1.0")
window.vertical_synchronization = True

# The tank should be created in the Game object
# tank = TankBody(sf.Texture.from_file("res/RectTankDetailed.png"))
# turret = TankTurret(sf.Texture.from_file("res/TankTurret.png"))

# tank = AssaultGunBody(sf.Texture.from_file("res/RectTankDetailed.png"))
# turret = AssaultGunTurret(sf.Texture.from_file("res/TankTurret.png"))
#
# g = Game(window=window, mouse=sf.Mouse, keyboard=sf.Keyboard)
# g.add_tank(tank)
#
#
# turret.set_body(tank)
# tank.set_turret(turret)
#
# tank.position = game_size / 2

m = MenuScreen(window)

stage = "Menu"

while window.is_open:
    # handle events
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()

    window.clear(sf.Color(50, 200, 50))
    # if g.is_playing:
    #
    #     g.update()
    #
    #     g.draw_objects()
    if stage == "Menu":
        m.update(sf.Mouse)
        m.draw_objects()
        if m.setup:
            stage = "Playing"
            game = m.game

    elif stage == "Playing":
        game.update()
        game.draw_objects()
    window.display()
