import unittest
import closest_coordinates as c


class TestCase(unittest.TestCase):
    def test1(self):
        # Check for origin(0,0)
        result = c.sort_coordinate([{'id': 'a', 'value': '31,49'}, {'id': 'b', 'value': '44,67'}], 0, 0)
        self.assertEqual(result, [{'id': 'a', 'value': '31,49'}, {'id': 'b', 'value': '44,67'}])

    def test2(self):
        # check for origin(-6,33)
        result = c.sort_coordinate([{'id': 'a', 'value': '31,49'}, {'id': 'b', 'value': '12,10'}], -6, 33)
        self.assertEqual(result, [{'id': 'b', 'value': '12,10'}, {'id': 'a', 'value': '31,49'}])

if __name__ == '__main__':
    unittest.main()

