import unittest
from game import get_available_moves, move_player, collect_item


class TestGame(unittest.TestCase):

    def test_beach_has_jungle_as_available_move(self):
        moves = get_available_moves("Beach")

        self.assertEqual(moves, ["Jungle"])

    def test_jungle_has_beach_and_cave_as_available_moves(self):
        moves = get_available_moves("Jungle")

        self.assertEqual(moves, ["Beach", "Cave"])

    def test_valid_move_reduces_energy(self):
        location, energy, moved = move_player(
            "Beach", "Jungle", 5, []
        )

        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_player_cannot_move_with_zero_energy(self):
        location, energy, moved = move_player(
            "Beach", "Jungle", 0, []
        )

        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 0)
        self.assertFalse(moved)

    def test_player_cannot_enter_old_bridge_without_rope(self):
        location, energy, moved = move_player(
            "Cave", "Old Bridge", 5, []
        )

        self.assertEqual(location, "Cave")
        self.assertEqual(energy, 5)
        self.assertFalse(moved)

    
    def test_player_cannot_enter_lighthouse_without_lantern(self):
        location, energy, moved = move_player(
            "Old Bridge", "Lighthouse", 5, ["Rope"]
        )

        self.assertEqual(location, "Old Bridge")
        self.assertEqual(energy, 5)
        self.assertFalse(moved)

    def test_player_can_enter_lighthouse_with_lantern(self):
        location, energy, moved = move_player(
            "Old Bridge", "Lighthouse", 5, ["Rope", "Lantern"]
        )

        self.assertEqual(location, "Lighthouse")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)


    def test_player_cannot_move_to_unconnected_location(self):
        location, energy, moved = move_player(
            "Beach", "Cave", 5, ["Rope", "Lantern"]
        )

        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertFalse(moved)


    def test_player_collects_rope_in_jungle(self):
        inventory = []

        item = collect_item("Jungle", inventory)

        self.assertEqual(item, "Rope")
        self.assertEqual(inventory, ["Rope"])


    def test_player_collects_lantern_in_cave(self):
        inventory = []

        item = collect_item("Cave", inventory)

        self.assertEqual(item, "Lantern")
        self.assertEqual(inventory, ["Lantern"])


    def test_player_cannot_collect_rope_twice(self):
        inventory = []

        first_collection = collect_item("Jungle", inventory)
        second_collection = collect_item("Jungle", inventory)

        self.assertEqual(first_collection, "Rope")
        self.assertIsNone(second_collection)
        self.assertEqual(inventory, ["Rope"])


    def test_player_cannot_collect_lantern_twice(self):
        inventory = []

        first_collection = collect_item("Cave", inventory)
        second_collection = collect_item("Cave", inventory)

        self.assertEqual(first_collection, "Lantern")
        self.assertIsNone(second_collection)
        self.assertEqual(inventory, ["Lantern"])


    def test_location_without_item_returns_none(self):
        inventory = []

        item = collect_item("Beach", inventory)

        self.assertIsNone(item)
        self.assertEqual(inventory, [])


    def test_last_energy_point_allows_one_valid_move(self):
        location, energy, moved = move_player(
            "Beach", "Jungle", 1, []
        )

        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 0)
        self.assertTrue(moved)

    def test_energy_never_becomes_negative(self):
        location, energy, moved = move_player(
            "Beach", "Jungle", 0, []
        )

        self.assertGreaterEqual(energy, 0)
        self.assertEqual(energy, 0)
        self.assertFalse(moved)

if __name__ == "__main__":
    unittest.main()
