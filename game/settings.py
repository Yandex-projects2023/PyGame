import math

# Настройки игры
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 100
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# Настройки миникарты
MINIMAP_SCALE = 6
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE  # 1 -> 12 x 8, 2 -> 24 x 16, 3 -> 36 x 24
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# Настройки RayCasting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# Настройки спрайтов
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# Настройки текстур (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# Настройки игрока
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_health = 100
player_angle = 0
player_speed = 1
player_stamina = 100  # Начальное значение выносливости
player_max_stamina = 100  # Максимальное значение выносливости
player_stamina_regen_rate = 5  # Скорость восстановления выносливости в единицах в секунду

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)

# Карта
MAZE_HEIGHT = 25
MAZE_WIDTH = MAZE_HEIGHT
# maze_width = int(maze_height * (25/15))