from queue import PriorityQueue
import copy

def location_of_zero(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return row, col

# 8-puzzle problem have only 4 possile actions
# up, down, left, and right.
# These actions are applied on the blank space i-e; 0
def actions(puzzle):
    action = []
    
    i, j = location_of_zero(puzzle)
    
    if i+1 <= 2:
        action.append('down')
    if i-1 >= 0:
        action.append('up')
    if j+1 <= 2:
        action.append('right')
    if j-1 >= 0:
        action.append('left')
    return action

def child_node(node, action):
    child = { 'state': copy.deepcopy(node) }
    
    i, j = location_of_zero(child['state'])
    
    if action == 'up':
        child['state'][i][j], child['state'][i-1][j] = child['state'][i-1][j], child['state'][i][j]
    elif action == 'down':
        child['state'][i][j], child['state'][i+1][j] = child['state'][i+1][j], child['state'][i][j]
    elif action == 'left':
        child['state'][i][j], child['state'][i][j-1] = child['state'][i][j-1], child['state'][i][j]
    elif action == 'right':
        child['state'][i][j], child['state'][i][j+1] = child['state'][i][j+1], child['state'][i][j]
    return child

def goal_test(puzzle):
    return puzzle == goal_state

def printPuzzle(puzzle):
    for row in puzzle:
        print("-------------")
        print("|",row[0],"|",row[1],"|", row[2], "|")
    print("-------------")

def distance(row, col, num):
    dist = 0
    r = num // 3
    c = num % 3
    
    while r != row:
        if r > row:
            row += 1
            dist += 1
        else:
            row -= 1
            dist += 1
    
    while c != col:
        if c > col:
            col += 1
            dist += 1
        else:
            col -= 1
            dist += 1      
    return dist

def manhatten_distance(puzzle):
    dist = 0
    
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] != 0:
                dist += distance(row, col, puzzle[row][col]-1)
    return dist