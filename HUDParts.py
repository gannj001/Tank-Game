__author__ = 'John'

import sfml as sf


class StatTracker(sf.Text):
    def __init__(self):
        sf.Text.__init__(self)
        self.stat = None
        self.string = "0"
        self.position = None
        self.font = sf.Font.from_file("res/neo_scifi.ttf")
        self.color = sf.Color.WHITE
        self.character_size = 20

    def set_tracked_stat(self, stat):
        self.stat = stat

    def set_position(self, position):
        self.position = position

    def set_string(self):
        self.string = self.encode_to_string()

    def encode_to_string(self):
        if isinstance(self.stat, bool):
            ret = self.parse_bool(self.stat)
        elif isinstance(self.stat, int):
            ret = self.parse_int(self.stat)
        elif isinstance(self.stat, list):
            ret = self.parse_list(self.stat)
        elif isinstance(self.stat, str):
            ret = self.stat
        else:
            ret = "Incompatible Argument"
        return ret

    @staticmethod
    def parse_bool(val):
        if val:
            return "True"
        else:
            return "False"

    @staticmethod
    def parse_int(val):
        return str(val)

    @staticmethod
    def parse_list(val):
        return ', '.join(val)

