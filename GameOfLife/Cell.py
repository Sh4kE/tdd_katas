class Cell(object):
    def __init__(self, alive=False):
        self.alive = alive

    def update(self, neighbours):
        if self.count_live_cells(neighbours) < 2:
            self.alive = False
        if self.count_live_cells(neighbours) > 3:
            self.alive = False
        if self.count_live_cells(neighbours) == 3:
            self.alive = True

    @staticmethod
    def count_live_cells(neighbours):
        return len([live_neighbour for live_neighbour in neighbours if live_neighbour.alive])

    def __str__(self):
        if self.alive:
            return "*"
        else:
            return "_"
