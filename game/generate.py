import numpy as np
from settings import *
import random


class PrimsMazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self, width, height):
        maze = np.zeros((height, width), dtype=bool)
        x = random.randrange(0, width // 2) * 2
        y = random.randrange(0, height // 2) * 2
        need_connect_points = set()
        need_connect_points.add((x, y))
        while need_connect_points:
            point = random.sample(list(need_connect_points), 1)[0]
            need_connect_points.remove(point)
            x, y = point
            maze[y, x] = True
            self.connect(maze, x, y)
            self.add_visit_points(maze, need_connect_points, x, y)
            fm = self.format_maze(maze)
        return fm

    def connect(self, maze, x, y):
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        random.shuffle(directions)
        for dx, dy in directions:
            neighbor_x = x + dx * 2
            neighbor_y = y + dy * 2
            if self.is_road(maze, neighbor_x, neighbor_y):
                connector_x = x + dx
                connector_y = y + dy
                maze[connector_y, connector_x] = True
                return

    def add_visit_points(self, maze, points, x, y):
        if self.is_point_in_maze(maze, x - 2, y) and not self.is_road(maze, x - 2, y):
            points.add((x - 2, y))
        if self.is_point_in_maze(maze, x + 2, y) and not self.is_road(maze, x + 2, y):
            points.add((x + 2, y))
        if self.is_point_in_maze(maze, x, y - 2) and not self.is_road(maze, x, y - 2):
            points.add((x, y - 2))
        if self.is_point_in_maze(maze, x, y + 2) and not self.is_road(maze, x, y + 2):
            points.add((x, y + 2))

    def format_maze(self, maze_link):
        form_maze = [[1 for _ in range(len(maze_link[0]) + 2)] for _ in range(len(maze_link) + 2)]
        for y in range(1, len(form_maze)-1):
            for x in range(1, len(form_maze[y])-1):
                if maze_link[y - 1][x - 1]:
                    form_maze[y][x] = False
                else:
                    form_maze[y][x] = 1
        return form_maze

    def is_road(self, maze, x, y):
        return maze[y, x] if 0 <= y < maze.shape[0] and 0 <= x < maze.shape[1] else False

    def is_point_in_maze(self, maze, x, y):
        return 0 <= y < maze.shape[0] and 0 <= x < maze.shape[1]

    def found_empty_space(self, maze):
        x, y = random.randint(1, MAZE_HEIGHT + 1), random.randint(0, MAZE_HEIGHT)
        while maze[y - 1][x - 1] == 1:
            x, y = random.randint(0, MAZE_HEIGHT), random.randint(0, MAZE_HEIGHT)
        return (x - 0.5, y - 0.5)
