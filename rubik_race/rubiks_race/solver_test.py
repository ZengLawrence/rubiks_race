'''
Created on Jun 27, 2017

@author: lawrencezeng
'''
import unittest
from rubiks_race import solver

class Test(unittest.TestCase):

    def setUp(self):
        self.initial_position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['g', 'o', ' ', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ]
        self.pattern = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'r'],
                         ['b', 'b', 'y']
                    ]
        
        final_positions = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ]
        moves = [
                 [[2, 1], [2, 2]],
                 [[2, 0], [2, 1]],
                 ]
        self.result = [final_positions, moves]
        
    def tearDown(self):
        return unittest.TestCase.tearDown(self)



    def test_solve(self):
        initial_position = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    ['g', 'o', ' ', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ]
        pattern = [
                         ['g', 'w', 'w'],
                         ['g', 'o', 'r'],
                         ['b', 'b', 'y']
                    ]
       
        
        final_positions = [
                    ['g', 'g', 'y', 'r', 'r' ],
                    ['w', 'g', 'w', 'w', 'y' ],
                    [' ', 'g', 'o', 'r', 'o' ],
                    ['o', 'b', 'b', 'y', 'y' ],
                    ['b', 'o', 'w', 'r', 'b' ]
                    ]
        moves = [
                 [[2, 1], [2, 2]],
                 [[2, 0], [2, 1]],
                 ]
        self.assertItemsEqual([final_positions, moves], solver.solve(initial_position, pattern))
        
    def test_solve_pq(self):
        self.assertItemsEqual(self.result, solver.solve_pq(self.initial_position, self.pattern))
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_solve']
    unittest.main()
