import copy

from Cell import Cell


class GameOfLife(object):
    def __init__(self, world_size=1000):
        self.world = [[Cell() for _ in range(world_size)] for _ in range(world_size)]

    def next_round(self):
        world_of_last_round = copy.deepcopy(self.world)
        for x in range(len(self.world)):
            for y in range(len(self.world[0])):
                neighbours = self.get_neighbours(world_of_last_round, x, y)
                self.world[x][y].update(neighbours)

    @staticmethod
    def get_neighbours(world, x, y):
        neighbours = []
        if x > 0:
            neighbours.append(world[x - 1][y])
        if x < len(world) - 1:
            neighbours.append(world[x + 1][y])
        if y > 0:
            neighbours.append(world[x][y - 1])
        if y < len(world[x]) - 1:
            neighbours.append(world[x][y + 1])
        if x > 0 and y > 0:
            neighbours.append(world[x - 1][y - 1])
        if x > 0 and y < len(world[x]) - 1:
            neighbours.append(world[x - 1][y + 1])
        if x < len(world) - 1 and y > 0:
            neighbours.append(world[x + 1][y - 1])
        if x < len(world) - 1 and y < len(world[x]) - 1:
            neighbours.append(world[x + 1][y + 1])
        return neighbours

    def __str__(self):
        board_representation = ""
        for row in self.world:
            for cell in row:
                board_representation += str(cell)
            board_representation += "\n"
        return board_representation


def add_glider():
    game_of_life.world[0][1].alive = True
    game_of_life.world[1][2].alive = True
    game_of_life.world[2][0].alive = True
    game_of_life.world[2][1].alive = True
    game_of_life.world[2][2].alive = True


def add_blinker():
    game_of_life.world[9][0].alive = True
    game_of_life.world[9][1].alive = True
    game_of_life.world[9][2].alive = True


if __name__ == '__main__':
    game_of_life = GameOfLife(world_size=25)
    add_glider()
    add_blinker()

    while True:
        print(game_of_life)
        game_of_life.next_round()
        print()
        print("#################################")
        print()
