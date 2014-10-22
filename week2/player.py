class Player:
    def __init__(self, name, entity, i, j):
        self.name = name
        self.entity = entity
        self.i = i
        self.j = j

    def set_position(self, i, j):
        self.i = i
        self.j = j
