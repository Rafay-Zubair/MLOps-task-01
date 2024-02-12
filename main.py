import eight_puzzle
import copy

initial_state = [
    [0, 1, 3],
    [4, 2, 5],
    [7, 8, 6]
]

print('Enter values for the initial state. (Values should be from 0 to 8, non-repeating)')

for i in range(3):
    for j in range(3):
        initial_state[i][j] = int(input(f"Enter for index {i}, {j} ==> "))

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("================INITIAL STATE=================")
eight_puzzle.printPuzzle(initial_state)
print("==============================================")

result, steps = eight_puzzle.heuristic_search(copy.deepcopy(initial_state), goal_state)

if result is None:
    print('No Solution exists.')
    print(':/')
else:
    print("==================FINAL STATE=================")
    eight_puzzle.printPuzzle(result)
    print('Total Steps:', steps)
    print("==============================================")