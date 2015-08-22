__author__ = 'John'

from HUDParts import StatTracker
from Destroyables import StationaryTarget
import sfml as sf
from random import randint


class Game:
    def __init__(self, window=None, mouse=None, keyboard=None):
        self.tanks = []
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.HUDObjects = []
        self.targets = []
        self.all_shells = []
        self.is_playing = True
        self.player_score = 0

        # HUD parts
        self.scorekeeper = None
        self.add_scorekeeper()
        self.reloaded = None

    def add_tank(self, tank):
        self.tanks.append(tank)

    def add_target(self, target):
        self.targets.append(target)

    def add_hud_parts(self, hudpart):
        self.HUDObjects.append(hudpart)

    def set_window(self, window):
        self.window = window

    def set_mouse(self, mouse):
        self.mouse = mouse

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard

    def add_scorekeeper(self):
        self.scorekeeper = StatTracker()
        self.scorekeeper.set_position((self.window.size.x/2, 10))
        self.add_hud_parts(self.scorekeeper)

    def add_reloaded_indicator(self):
        self.reloaded = StatTracker()
        self.reloaded.set_position((self.window.size.x*0.9, self.window.size.y*0.9))
        self.add_hud_parts(self.reloaded)

    def draw_objects(self):
        for tank in self.tanks:
            self.window.draw(tank)
            for shell in tank.turret.shells:
                self.window.draw(shell)
            self.window.draw(tank.turret)

        for target in self.targets:
            self.window.draw(target)

        for part in self.HUDObjects:
            self.window.draw(part)

    def new_target(self):
        if len(self.targets) < 5:
            t = StationaryTarget(sf.Texture.from_file("res/Target.png"))
            xcoord = randint(10, 20)
            ycoord = randint(10, 20)
            t.set_position = self.window.size/2


    def update(self):
        for tank in self.tanks:
            tank.update(self.mouse, self.window, self.keyboard)

        for target in self.targets:
            for tank in self.tanks:
                target.update(tank.turret.shells)
            if not target.alive:
                self.targets.remove(target)
                self.player_score += 1

        self.new_target()

        self.scorekeeper.string = str(self.player_score)
