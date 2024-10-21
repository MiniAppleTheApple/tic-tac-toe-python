import unittest
import main

class TestTicTacToe(unittest.TestCase):
    
    def test_winning_by_column(self):
        table = [
            "x", "x", "x",
            " ", " ", " ",
            " ", " ", " ",
        ]

        self.assertTrue(main.is_any_player_winned_by_column(table, "x"))

    def test_winning_by_row(self):
        table = [
            "x", " ", " ",
            "x", " ", " ",
            "x", " ", " ",
        ]

        self.assertTrue(main.is_any_player_winned_by_row(table, "x"))

    def test_winning_by_slope(self):
        table = [
            "x", " ", " ",
            " ", "x", " ",
            " ", " ", "x",
        ]

        self.assertTrue(main.is_any_player_winned_by_slope(table, "x"))

    def test_is_filled(self):
        table = [
            "x", "o", "x",
            "o", "o", "x",
            "x", "x", "o",
        ]

        self.assertTrue(main.is_filled(table))
    
    def test_format_table(self):
        table = [
            "x", "o", "x",
            "o", "o", "x",
            "x", "x", "o",

        ]

        expected = """|x|o|x|
|o|o|x|
|x|x|o|"""
        self.assertEqual(main.text_format_table(table), expected)




if __name__ == "__main__":
    unittest.main()
