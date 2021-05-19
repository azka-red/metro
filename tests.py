    """
    test.py evals some test data with the actual important functions of metro.py
    and compares it with several case uses defined as global variables below.
    You can change the value of this variables as you see fit.    
    """

import unittest
from loadfile import load_file
from metro import find_all_paths, find_best_routes

#URLs for test data

TEST_FILE_1 = "test_data/test1.graph"
TEST_FILE_2 = "test_data/test2.graph"
TEST_FILE_3 = "test_data/test3.graph"
TEST_FILE_4 = "test_data/test4.graph"


# Asuming the test files from above load data correcly, they must be equal to this
TEST_GRAPH_1 = {'A': {'connects_to': ['B'], 'color': 'white'}, 'B': {'connects_to': ['C'], 'color': 'white'}, 'C': {'connects_to': ['D', 'G'], 'color': 'white'}, 'D': {'connects_to': ['E'], 'color': 'white'}, 'E': {
    'connects_to': ['F'], 'color': 'white'}, 'F': {'connects_to': [''], 'color': 'white'}, 'G': {'connects_to': ['H'], 'color': 'green'}, 'H': {'connects_to': ['I'], 'color': 'red'}, 'I': {'connects_to': ['F'], 'color': 'green'}}

# Correct paths notation as a lists of lists
TEST_PATHS_1 = [['A', 'B', 'C', 'D', 'E', 'F'],
                ['A', 'B', 'C', 'G', 'H', 'I', 'F']]

#correct tuple of list representing best red, green and white paths
BEST_WHITE_PATHS = ([['A', 'B', 'C', 'D', 'E', 'F']],
                    [['A', 'B', 'C', 'D', 'E', 'F']])

BEST_RED_PATHS = ([['A', 'B', 'C', 'G', 'H', 'I', 'F']],
                  [['A', 'B', 'C', 'H', 'F']])

BEST_GREEN_PATHS = ([['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'G', 'H', 'I', 'F']], [
                    ['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'G', 'I', 'F']])


class TestLoadFile(unittest.TestCase):

    def test_load(self):

        print("Testing normal file loading")
        self.assertEqual(load_file(TEST_FILE_1), TEST_GRAPH_1,
                         "Graph returned incorrect layout, should be : "+str(TEST_GRAPH_1))

    def test_comment_proccesing(self):
        print("Testing file loading with some comments")
        self.assertEqual(load_file(TEST_FILE_2), TEST_GRAPH_1,
                         "Graph returned incorrect layout, should be : "+str(TEST_GRAPH_1))

    def test_white_lines(self):
        print("Testing file with white lines before and after")
        self.assertEqual(load_file(TEST_FILE_3), TEST_GRAPH_1,
                         "Graph returned incorrect layout, should be : "+str(TEST_GRAPH_1))

    def test_lines_with_not_valid_color(self):
        print("Testing file with garbage data as color data(not green or red)")
        self.assertEqual(load_file(TEST_FILE_4), TEST_GRAPH_1,
                         "Graph returned incorrect layout, should be : "+str(TEST_GRAPH_1))

    def test_path_finding(self):
        print("Testing path finding")
        self.assertEqual(find_all_paths(TEST_GRAPH_1, 'A', 'F'), TEST_PATHS_1,
                         "Pathfinding bugged. Should be : "+str(TEST_PATHS_1))

    def test_red_paths(self):
        print("Testing best red paths output")
        self.assertEqual(find_best_routes(TEST_GRAPH_1, TEST_PATHS_1, "red"), BEST_RED_PATHS,
                         "Optimal red path finding bugged, should be :" + str(BEST_RED_PATHS))

    def test_green_paths(self):
        print("Testing best green paths output")
        self.assertEqual(find_best_routes(TEST_GRAPH_1, TEST_PATHS_1, "green"), BEST_GREEN_PATHS,
                         "Optimal green path finding bugged, should be :" + str(BEST_GREEN_PATHS))

    def test_white_paths(self):
        print("Testing best white paths output")
        self.assertEqual(find_best_routes(TEST_GRAPH_1, TEST_PATHS_1, "white"), BEST_WHITE_PATHS,
                         "Optimal white path finding bugged, should be :" + str(BEST_WHITE_PATHS))


if __name__ == '__main__':
    unittest.main()
