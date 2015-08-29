__author__ = 'John'

import random

from Player import *
from HUDParts import StatTracker
from Destroyables import StationaryTarget
from EnemyTank import create_enemy_tank


class Game:
    def __init__(self, window=None, mouse=None, keyboard=None):
        self.tanks = []
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.HUDObjects = {}
        self.targets = []
        self.all_shells = []
        self.enemies = []
        self.objects = []
        self.is_playing = True
        self.player_score = 0
        self.window_size = sf.Vector2(800, 600)
        self.clock = sf.Clock()

        # HUD parts
        self.scorekeeper = None
        self.add_scorekeeper()
        self.reloaded = None
        self.timer = None
        self.add_timer()
        self.acc_display = None
        self.score_display = None

    def add_tank(self, tank):
        self.tanks.append(tank)
        self.objects.append(tank)

    def add_target(self, target):
        self.targets.append(target)
        self.objects.append(target)

    def add_hud_parts(self, hudpart, partname):
        self.HUDObjects[partname] = hudpart

    def set_window(self, window):
        self.window = window

    def set_mouse(self, mouse):
        self.mouse = mouse

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard

    def add_scorekeeper(self):
        self.scorekeeper = StatTracker()
        self.scorekeeper.set_position((self.window.size.x/2, 10))
        self.add_hud_parts(self.scorekeeper, "scorekeeper")

    def add_reloaded_indicator(self):
        self.reloaded = StatTracker()
        self.reloaded.set_position((self.window.size.x*0.9, self.window.size.y*0.9))
        self.add_hud_parts(self.reloaded, "reload_indicator")

    def add_enemy(self):
        tank = create_enemy_tank()
        tank.position = sf.Vector2(100, 100)
        self.enemies.append(tank)

    def new_target(self):
        if len(self.targets) < 5:
            t = StationaryTarget(sf.Texture.from_file("res/Target.png"))
            xcoord = random.random() * (self.window.size.x - t.local_bounds.width)
            ycoord = random.random() * (self.window.size.y - t.local_bounds.height)
            coords = sf.Vector2(xcoord, ycoord)
            t.position = coords
            self.targets.append(t)

    def add_timer(self):
        self.timer = StatTracker()
        self.timer.set_position((400, 550))
        self.add_hud_parts(self.timer, "timer")

    def draw_objects(self):
        for tank in self.tanks:
            self.window.draw(tank)
            for shell in tank.turret.shells:
                self.window.draw(shell)
            self.window.draw(tank.turret)

        for enemy in self.enemies:
            self.window.draw(enemy)
            for shell in enemy.turret.shells:
                self.window.draw(shell)
            self.window.draw(enemy.turret)

        for target in self.targets:
            self.window.draw(target)

        for name, part in self.HUDObjects.iteritems():
            self.window.draw(part)

    def score_screen(self):
        self.HUDObjects.clear()
        # This needs to change as more shells/tanks/turrets are introduced
        for tank in self.tanks:
            if isinstance(tank, PlayerTank) or isinstance(tank, PlayerGun):
                accuracy = 0
                if tank.turret.shells_fired != 0:
                    accuracy = self.player_score / self.tanks[0].turret.shells_fired * 100
        self.acc_display = StatTracker()
        self.acc_display.string = "Player Accuracy: " + str(accuracy)
        self.add_hud_parts(self.acc_display, "acc_display")
        self.acc_display.origin = self.acc_display.local_bounds.center
        self.acc_display.position = (self.window.size.x / 2, self.window.size.y / 3)
        self.score_display = StatTracker()
        self.score_display.origin = self.acc_display.local_bounds.center
        self.score_display.string = "Player Score: " + str(self.player_score)
        self.add_hud_parts(self.score_display, "score_display")
        self.score_display.position = (self.window.size.x / 2, self.window.size.y / 3 * 2)

    def update(self):
        if self.is_playing:
            for tank in self.tanks:
                tank.update(self.mouse, self.window, self.keyboard)
            for enemy in self.enemies:
                enemy.update(self.objects)
            if len(self.targets) > 0:
                for target in self.targets:
                    for tank in self.tanks:
                        target.update(tank.turret.shells)
                    if not target.alive:
                        self.targets.remove(target)
                        self.player_score += 1

            self.new_target()

            self.scorekeeper.string = str(self.player_score)
            time = self.clock.elapsed_time.seconds
            self.timer.string = str(round(time, 2))
            # if time >= 10.:
            #     self.is_playing = False
            #     self.score_screen()
