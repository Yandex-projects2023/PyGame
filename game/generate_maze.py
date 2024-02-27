import random

def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]
    # начальная точка
    x, y = random.randint(1, width - 2), random.randint(1, height - 2)
    maze[x][y] = 1
    # генерируем лабиринт
    while True:
        # выбираем ячейку с наименьшим количеством соседних стен
        min_neighbors = width  *  height
        x, y = None, None
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                neighbors = (maze[i - 1][j] + maze[i + 1][j] + maze[i][j - 1] + maze[i][j + 1]) & 1
                if neighbors < min_neighbors:
                    min_neighbors = neighbors
                    x, y = i, j
        if min_neighbors == 0:
            break
        maze[x][y] = 1
    return maze

# Пример использования
maze = generate_maze(10, 10)
for row in maze:
    print(row)