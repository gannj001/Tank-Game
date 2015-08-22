__author__ = 'John'


class Game:
    def __init__(self):
        self.tanks = []
        self.window = None
        self.mouse = None
        self.keyboard = None
        self.HUDObjects = []
        self.targets = []
        self.all_shells = []
        self.is_playing = True

    def add_tank(self, tank):
        self.tanks.append(tank)

    def add_target(self, target):
        self.targets.append(target)

    def add_HUD_parts(self, HUDPart):
        self.HUDObjects.append(HUDPart)

    def set_window(self, window):
        self.window = window

    def set_mouse(self, mouse):
        self.mouse = mouse

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard

    def draw_objects(self):
        for tank in self.tanks:
            self.window.draw(tank)
            for shell in tank.turret.shells:
                self.window.draw(shell)
            self.window.draw(tank.turret)

        for target in self.targets:
            self.window.draw(target)

        for HUDPart in self.HUDObjects:
            HUDPart.update()

    def aggregate_shells(self):
        for tank in self.tanks:
            yield self.all_shells.extend(tank.turret.shells)

    def update(self):
        for tank in self.tanks:
            tank.update(self.mouse, self.window, self.keyboard)
        self.aggregate_shells()
        for target in self.targets:
            for tank in self.tanks:
                target.update(tank.turret.shells)
            if not target.alive:
                self.targets.remove(target)
