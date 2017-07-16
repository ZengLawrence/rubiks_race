'''
Created on Jun 24, 2017

@author: lawrencezeng
'''
import unittest
from rubiks_race import game

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_position_matches_goal_should_return_true(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        goal = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'r'],
                         ['b', 'b', 'y']
                    ];
        self.assertTrue(game.is_goal(position, goal))

    def test_position_does_not_match_goal_should_return_false(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        goal = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'b'],
                         ['b', 'b', 'y']
                    ];
        self.assertFalse(game.is_goal(position, goal))

    def test_mismatched_tiles_when_position_matches_goal_should_return_0(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        goal = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'r'],
                         ['b', 'b', 'y']
                    ];
        self.assertEqual(0, game.mismatched_tiles(position, goal))

    def test_mismatched_tiles_position_does_not_match_goal_should_return_number_of_tiles_matched(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        goal = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'b'],
                         ['b', 'b', 'y']
                    ];
        self.assertEqual(1, game.mismatched_tiles(position, goal))
        
    def test_legal_moves_center_space_should_return_4_moves_down_left_right_up(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['g', 'o', ' ', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        to = [2,2]
        move_down  = [[1, 2], to]
        move_right = [[2, 1], to]
        move_left  = [[2, 3], to]
        move_up    = [[3, 2], to]
        moves = [
                 move_down,
                 move_left,
                 move_right,
                 move_up,
                 ];
        
        self.assertItemsEqual(moves, game.legal_moves(position))
        
    def test_legal_moves_space_on_left_edge_should_return_3_moves_down_right_up(self):
        position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', ' o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        to = [2,0]
        move_down  = [[1, 0], to]
        move_right = [[2, 1], to]
        move_up    = [[3, 0], to]
        moves = [
                 move_down,
                 move_right,
                 move_up,
                 ];
        
        self.assertItemsEqual(moves, game.legal_moves(position))
        
    def test_legal_moves_space_on_top_edge_should_return_3_moves_left_right_up(self):
        position = [
                    ['g', 'g', ' ', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['y', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        to = [0,2]
        move_right = [[0, 1], to]
        move_left  = [[0, 3], to]
        move_up    = [[1, 2], to]
        moves = [
                 move_left,
                 move_right,
                 move_up,
                 ];
        
        self.assertItemsEqual(moves, game.legal_moves(position))
        
    def test_legal_moves_space_on_right_edge_should_return_3_moves_down_right_up(self):
        position = [
                    ['g', 'g', 'o', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['y', 'g', 'o', 'r', ' ' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ];
        to = [2,4]
        move_down  = [[1, 4], to]
        move_right = [[2, 3], to]
        move_up    = [[3, 4], to]
        moves = [
                 move_down,
                 move_right,
                 move_up,
                 ];
        
        self.assertItemsEqual(moves, game.legal_moves(position))
        
    def test_legal_moves_space_on_bottom_edge_should_return_3_moves_down_left_right(self):
        position = [
                    ['g', 'g', 'o', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['y', 'g', 'o', 'r', 'w' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', ' ', 'r', 'b' ]
                    ];
        to = [4,2]
        move_down  = [[3, 2], to]
        move_right = [[4, 1], to]
        move_left  = [[4, 3], to]
        moves = [
                 move_down,
                 move_right,
                 move_left,
                 ];
        
        self.assertItemsEqual(moves, game.legal_moves(position))
        
    def test_move_from_a_posiont_with_1_move_should_return_new_position_after_the_move_applied(self):
        before_position = [
                    ['g', 'g', 'o', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['y', 'g', 'o', 'r', 'w' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', ' ', 'r', 'b' ]
                    ];
        a_move = [[3,2], [4,2]];
        
        after_position = [
                    ['g', 'g', 'o', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['y', 'g', 'o', 'r', 'w' ],
                    ['o', 'b', ' ', 'y', 'y' ],
                    ['b', 'o', 'b', 'r', 'b' ]
                    ];
        self.assertItemsEqual(after_position, game.move(before_position, a_move))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()