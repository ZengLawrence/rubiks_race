'''
Created on Jun 22, 2017

@author: lawrencezeng
'''
from rubiks_race import solver

def start():
    
    initial_position = [
                ['g', 'g', 'y', 'r', 'r' ],
                ['w', 'g', 'w', 'w', 'y' ],
                ['o', 'o', ' ', 'b', 'o' ],
                ['o', 'b', 'b', 'y', 'y' ],
                ['b', 'g', 'w', 'r', 'r' ]
                ]
    
    pattern = [
                     ['w', 'b', 'g'],
                     ['r', 'g', 'o'],
                     ['w', 'b', 'g']
                ]
    
    solver.play_game(initial_position, pattern)
    
def fast_puzzle():
    initial_position = [
                ['g', 'g', 'y', 'r', 'r' ],
                ['w', 'g', 'w', 'w', 'y' ],
                ['o', 'o', ' ', 'b', 'o' ],
                ['o', 'b', 'b', 'y', 'y' ],
                ['b', 'g', 'w', 'r', 'r' ]
                ]
    
    pattern = [
                     ['g', 'w', 'w'],
                     ['g', 'o', 'r'],
                     ['b', 'b', 'y']
                ]
    solver.play_game(initial_position, pattern)
    
if __name__ == '__main__':
    fast_puzzle()
