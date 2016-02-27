import unittest

from GameOfLife import GameOfLife


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.game_of_life = GameOfLife(world_size=10)

    def test_can_create_gol(self):
        self.assertIsNotNone(self.game_of_life)

    def test_get_current_world(self):
        self.assertIsNotNone(self.game_of_life.world)

    def test_initially_all_cells_dead(self):
        for row in self.game_of_life.world:
            for cell in row:
                self.assertFalse(cell.alive)

    def test_live_cell_with_fewer_than_two_live_neighbours_dies_in_next_round(self):
        self.game_of_life.world[0][0].alive = True
        self.game_of_life.next_round()
        self.assertFalse(self.game_of_life.world[0][0].alive)

    def test_live_cell_with_more_than_three_live_neighbours_dies_in_next_round(self):
        self.game_of_life.world[1][1].alive = True

        self.game_of_life.world[0][1].alive = True
        self.game_of_life.world[1][0].alive = True
        self.game_of_life.world[2][1].alive = True
        self.game_of_life.world[1][2].alive = True

        self.game_of_life.next_round()

        self.assertFalse(self.game_of_life.world[1][1].alive)

    def test_live_cell_with_two_live_neighbours_lives_on_to_the_next_generation(self):
        self.game_of_life.world[1][1].alive = True

        self.game_of_life.world[0][1].alive = True
        self.game_of_life.world[1][0].alive = True

        self.game_of_life.next_round()

        self.assertTrue(self.game_of_life.world[1][1].alive)

    def test_live_cell_with_three_live_neighbours_lives_on_to_the_next_generation(self):
        self.game_of_life.world[1][1].alive = True

        self.game_of_life.world[0][1].alive = True
        self.game_of_life.world[1][0].alive = True
        self.game_of_life.world[2][1].alive = True

        self.game_of_life.next_round()

        self.assertTrue(self.game_of_life.world[1][1].alive)

    def test_dead_cell_with_exactly_three_live_neighbours_becomes_a_live_cell(self):
        self.game_of_life.world[0][1].alive = True
        self.game_of_life.world[1][0].alive = True
        self.game_of_life.world[2][1].alive = True

        self.game_of_life.next_round()

        self.assertTrue(self.game_of_life.world[1][1].alive)

if __name__ == '__main__':
    unittest.main()
