__author__ = 'John'

import sfml as sf

from Game import Game
from Button import Button
from Player import PlayerTank, PlayerGun
from TextBox import TextBox


class MenuScreen:
    def __init__(self, window):
        self.tank_type = None
        self.window = None
        self.button_dict = {}
        self.tank_chosen = False
        self.setup = False
        self.window = window
        self.setup_menu_screen()
        self.game = None

    def create_game(self):
        self.game = Game(window=self.window, mouse=sf.Mouse, keyboard=sf.Keyboard)
        if self.tank_type == 'assaultgun':
            tank = PlayerGun(sf.Texture.from_file("res/AssaultGunDetailed.png"))
        else:
            tank = PlayerTank(sf.Texture.from_file("res/RectTankDetailed.png"))

        tank.position = (self.window.size / 2)
        self.game.add_tank(tank)
        self.game.add_enemy()
        self.game.add_obstacles()

    def setup_menu_screen(self):
        title = TextBox(sf.Texture.from_file("res/title.png"))
        title.origin = title.local_bounds.center
        title.set_position((self.window.size.x / 2, (self.window.size.y / 3)))
        self.button_dict['title'] = title

        assaultgunbutton = Button(sf.Texture.from_file("res/AssaultGunButton.png"))
        assaultgunbutton.origin = assaultgunbutton.local_bounds.center
        assaultgunbutton.set_position(self.window.size / 2)
        self.button_dict['assaultgun'] = assaultgunbutton

        tankbutton = Button(sf.Texture.from_file("res/TankButton.png"))
        tankbutton.origin = tankbutton.local_bounds.center
        tankbutton.set_position((self.window.size.x / 2, (self.window.size.y / 3) * 2))
        self.button_dict['tank'] = tankbutton

    def set_tank_type(self, tank_type):
        self.tank_type = tank_type

    def set_window(self, window):
        self.window = window

    def draw_objects(self):
        for key, val in self.button_dict.iteritems():
            self.window.draw(val)

    def update(self, mouse):
        if mouse.is_button_pressed(sf.Mouse.LEFT):
            for key, val in self.button_dict.iteritems():
                val.update(mouse.get_position(self.window))
                if val.clicked:
                    print key, "chosen!"
                    self.tank_chosen = True
                    self.set_tank_type(key)
                    self.create_game()
                    self.setup = True
