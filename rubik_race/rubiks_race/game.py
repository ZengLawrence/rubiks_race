'''
Created on Jun 24, 2017

@author: lawrencezeng
'''

def is_goal(position, goal):
    
    for i in xrange(0, len(goal)):
        for j in xrange(0, len(goal[0])):
            if position[i + 1][j + 1] != goal[i][j]:
                return False
    
    return True

def mismatched_tiles(position, goal):
    """ Return number of mismatched tiles"""
    mismatched = 0
    for i in xrange(0, len(goal)):
        for j in xrange(0, len(goal[0])):
            if position[i + 1][j + 1] != goal[i][j]:
                mismatched = mismatched + 1
    
    return mismatched

def legal_moves(position, current_space_cell = None):
    
    space_cell = current_space_cell or _find_space_tile(position)
     
    moves = list()
    _append_move_if_valid(moves, _above(space_cell), space_cell)
    _append_move_if_valid(moves, _left_of(space_cell), space_cell)
    _append_move_if_valid(moves, _right_of(space_cell), space_cell)
    _append_move_if_valid(moves, _below(space_cell), space_cell)
    
    return moves

def _find_space_tile(position):
    for i, row in enumerate(position):
        for j, tile in enumerate(row):
            if (tile == ' '):
                return [i, j]

def _left_of(cell):
    x, y = cell
    return [x, y - 1]

def _right_of(cell):
    x, y = cell
    return [x, y + 1]

def _above(cell):
    x, y = cell
    return [x - 1, y]

def _below(cell):
    x, y = cell
    return [x + 1, y]

def _is_valid_cell(cell):
    x, y = cell
    return (( x >= 0 and x < 5) and ( y >= 0 and y < 5))

def _append_move_if_valid(moves, from_cell, to_cell):
    if (_is_valid_cell(from_cell)):
        move = [from_cell, to_cell]
        moves.append(move)
    
    
def move(a_postion, a_move):   
    from_xy, to_xy = a_move
    fr_x, fr_y = from_xy
    to_x, to_y = to_xy
    after_position = list(a_postion)
    after_position[to_x] = _replace(after_position[to_x], to_y, a_postion[fr_x][fr_y])
    if fr_x == to_x:
        after_position[fr_x][fr_y] = a_postion[to_x][to_y]
    else:
        after_position[fr_x] = _replace(after_position[fr_x], fr_y, a_postion[to_x][to_y])
    return after_position


def _replace(row, i, value):
    copied_row = list(row)
    copied_row[i] = value
    return copied_row