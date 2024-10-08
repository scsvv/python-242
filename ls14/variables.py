from pygame.locals import Rect, QUIT
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT
from pygame.locals import K_w, K_s, K_d, K_a


# SIZE
WINDOWS_SIZE = (1080, 720)
DEFAULT_OBJ_SIZE = (30, 30)


# COLORS:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# POSITINAL
SPAWN_COORDINATE = (400, 300)
APPLE_SPAWN_COORDINATE = (700, 300)

BODY_SPAWN_COORDINATE = (
    SPAWN_COORDINATE[0] - DEFAULT_OBJ_SIZE[0], 
    SPAWN_COORDINATE[1]
    )

SPEED = DEFAULT_OBJ_SIZE[0]
DIRECTION = [SPEED, 0]
SCORE = 0
