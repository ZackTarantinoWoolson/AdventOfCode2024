import os
import sys
from copy import deepcopy

p = open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt")).read().split('\n')
puzzle = []

for i in p:
    puzzle.append([j for j in i])

def direction(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] in '^v><':
                return puzzle[i][j]
def starting(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] in '^v><':
                return (i, j)
ans = 0
start = starting(puzzle)
dir = direction(puzzle)
puzzle2 = deepcopy(puzzle)

def walkGuard(grid, start, dir):
    pos = start
    dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    prevPos = start
    walking = True
    # Add 'X' until you reach a '#'.
    while walking:
        prevPos = pos
        pos = tuple(map(lambda i, j: i + j, pos, dirs[dir]))
        if (pos[0] > (len(grid) - 1)) or (pos[1] > (len(grid[0]) - 1)) or (pos[0] < 0) or (pos[1] < 0):
            return False
        if grid[pos[0]][pos[1]] == '#':
            walking = False
            if dir == '>':
                dir = 'v'
                walkGuard(grid, prevPos, dir)
            elif dir == 'v':
                dir = '<'
                walkGuard(grid, prevPos, dir)
            elif dir == '<':
                dir = '^'
                walkGuard(grid, prevPos, dir)
            elif dir == '^':
                dir = '>'
                walkGuard(grid, prevPos, dir)
        if (pos[0] > (len(grid) - 1)) or (pos[1] > (len(grid[0]) - 1)):
            return False


for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        puzzle2[i][j] = '#'
        try:
            walkGuard(puzzle2, start, dir)
            puzzle2 = deepcopy(puzzle)
        except RecursionError:
            puzzle2 = deepcopy(puzzle)
            ans += 1


print(f'Part Two: {ans}')