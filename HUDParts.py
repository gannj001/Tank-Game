__author__ = 'John'

import sfml as sf


class StatTracker(sf.Text):
    def __init__(self):
        sf.Text.__init__(self)
        self.stat = None
        self.string = "0"
        self.position = None
        self.font = sf.Font.from_file("res/neo_scifi.ttf")

    def set_tracked_stat(self, stat):
        self.stat = stat

    def set_position(self, position):
        self.position = position

    def set_string(self):
        output = self.encode_to_string()
        self.string = output

    def encode_to_string(self):
        if type(self.stat) == "bool":
            ret = self.parse_bool(self.stat)
        elif type(self.stat) == "int":
            ret = self.parse_int(self.stat)
        elif type(self.stat) == "list":
            ret = self.parse_list(self.stat)
        elif type(self.stat) == "string":
            ret = self.stat
        else:
            ret = "Incompatible Argument"
        return ret

    def parse_bool(self, val):
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

    def update(self):
        self.set_string()
