'''
Created on Jun 27, 2017

@author: lawrencezeng
'''
import game
from _collections import deque
import time
import datetime
from _heapq import heappush, heappop, nsmallest


def solve(initial_position, pattern):
    
    initial_moves = []
    position_moves = [initial_position, initial_moves]
    queue = deque([position_moves])
    level = 0
    seen = set()
    while (len(queue) >0 ):
        print "starting level ", level, "No. of positions", len(queue)
        next_queue = deque([])
        for curr_position, prev_moves in queue:
            if game.is_goal(curr_position, pattern):
                return [curr_position, prev_moves]
            current_space_cell = None
            if len(prev_moves) > 0:
                current_space_cell, _ = prev_moves[-1]
            for move in game.legal_moves(curr_position, current_space_cell):
                if len(prev_moves) > 0 and _is_reverse_move(move, prev_moves[-1]):
                    continue
                next_position = game.move(curr_position, move)
                nps = _position_as_string(next_position)
                if (nps in seen):
                    continue
                moves = list(prev_moves)
                moves.append(move)
                next_queue.append([next_position, moves])
            seen.add(_position_as_string(curr_position))
        queue = next_queue
        level = level + 1
        
    return position_moves

def solve_pq(initial_position, pattern):
    """Solve using priority queue """
    
    initial_moves = []
    if game.is_goal(initial_position, pattern):
        return [initial_position, initial_moves]
    
    position_moves = [0, 0, 0, initial_position, initial_moves]
    queue = [position_moves]
    level = 0
    seen = set()
    while (len(queue) > 0):
        print "starting level ", level, "No. of positions", len(queue)
        next_queue = []
        for i, item in enumerate(queue):
            _, _, _, curr_position, prev_moves = item
            for j, move in enumerate(game.legal_moves(curr_position)):
                if len(prev_moves) > 0 and _is_reverse_move(move, prev_moves[-1]):
                    continue
                next_position = game.move(curr_position, move)
                nps = _position_as_string(next_position)
                if (nps in seen):
                    continue
                moves = list(prev_moves)
                moves.append(move)
                if game.is_goal(next_position, pattern):
                    return [next_position, moves]
                priority = _score(next_position, pattern)
                heappush(next_queue, [priority, i, j, next_position, moves])
            seen.add(_position_as_string(curr_position))
        
        queue = nsmallest(10000, next_queue)
        level = level + 1
        
    return position_moves

def _score(position, goal):
    """Score how close position is to the goal.  Lower the score the better.  If perfect match, the score is 0. """
    
    score = 0
    for i in xrange(0, len(goal)):
        for j in xrange(0, len(goal[0])):
            tile_value = goal[i][j]
            position_cell = _tranlate_to_position_cell(i, j)
            if _match_position(position_cell, position, tile_value):
                score = score + 0
            elif _match_adjacent(position_cell, position, tile_value):
                score = score + 0.5
            elif _match_corners(position_cell, position, tile_value):
                score = score + 0.75
            else:
                score = score + 1
    
    return score

def _match_position(position_cell, position, tile_value):
    x, y = position_cell
    return position[x][y] == tile_value
    
def _match_adjacent(position_cell, position, tile_value):
    x, y = position_cell
    return (position[x-1][y] == tile_value or position[x+1][y] == tile_value or position[x][y-1] == tile_value or position[x][y+1] == tile_value)
    
def _match_corners(position_cell, position, tile_value):
    x, y = position_cell
    return (position[x-1][y-1] == tile_value or position[x-1][y+1] == tile_value or position[x+1][y-1] == tile_value or position[x+1][y+1] == tile_value)
    
def _tranlate_to_position_cell(x, y):
    return [x + 1, y + 1]
    
def _is_reverse_move(m1, m2):
    return (m1[0] == m2[1]) and (m1[1] == m2[0])
    
def _position_as_string(position):
    s = ""
    for row in position:
        for cell in row:
            s = s + cell
    return s

def play_game(initial_position, pattern):
    """ Solve puzzle and print out results """
    
    _print_position(initial_position, "Initial Position")
    _print_position(pattern, "Pattern")
    
    # solving the puzzle
    start_time = time.time()
    #final_postion, moves = solve(initial_position, pattern)
    final_postion, moves = solve_pq(initial_position, pattern)
    elapsed_seconds = time.time() - start_time
    
    _print_position(final_postion, "Final Position")
    _print_moves(moves, elapsed_seconds)

def _print_position(positon, title):
    print title
    x_lable = ""
    spaces = " " * 4
    for i in range(len(positon[0])):
        x_lable = x_lable + spaces + str(i)
    print x_lable
    for i, row in enumerate(positon):
        print i, row
    print

def _print_moves(moves, elapsed_seconds):   
    print
    print "Solution:", len(moves), "moves", "time: ", str(datetime.timedelta(seconds=elapsed_seconds))
    for from_cell, to_cell in moves:
        print from_cell, "->", to_cell
    print
