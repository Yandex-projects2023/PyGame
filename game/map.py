from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32
from random import choice

_ = False
# matrix_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, 1],
#     [1, _, 2, 2, _, _, _, _, _, 2, 2, 2, _, _, _, 3, _, _, _, _, 4, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, 3, _, _, _, _, _, _, 1],
#     [1, _, 2, 2, _, _, _, _, _, _, _, _, 2, _, 4, _, _, 3, _, _, _, 4, _, 1],
#     [1, _, _, _, _, _, 4, _, _, 2, 2, _, 2, _, _, _, _, _, _, 4, _, _, _, 1],
#     [1, _, 3, _, _, _, 2, _, _, 2, _, _, 2, _, _, _, 4, _, _, _, _, 4, _, 1],
#     [1, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, 3, _, _, _, _, _, _, _, 3, _, _, 3, 3, _, _, _, _, 3, 3, _, _, 1],
#     [1, _, 3, _, _, _, 3, 3, _, 3, _, _, _, 3, 3, _, _, _, _, 2, 3, _, _, 1],
#     [1, _, _, _, _, 3, _, 3, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, 4, _, 3, _, _, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, 2, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, 2, _, _, _, _, _, _, 2, 2, _, 1],
#     [1, _, _, 4, _, _, _, _, 4, _, _, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]


def generate_maze(height, width):
    maze = []
    for _ in range(height):
        row = [0] * width
        maze.append(row)

    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                maze[i][j] = 1
            else:
                maze[i][j] = choice([False, 1])
    return maze


matrix_map = list(generate_maze(15, 24))
for i in matrix_map:
    print(i)

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4