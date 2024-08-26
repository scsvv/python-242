import pygame
from variables import * 
from sys import exit

# Pygame Initialization 
pygame.init()

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, DEFAULT_OBJ_SIZE)
    rect = image.get_rect(center=(x, y))
    transpet = image.get_at((0, 0))
    image.set_colorkey(transpet)

    return image, rect


def move(snake, direction):
    key = pygame.key.get_pressed()

    if key[K_UP] or key[K_w]: 
        direction = [0, -SPEED]
    elif key[K_DOWN] or key[K_s]:
        direction = [0, SPEED]
    elif key[K_LEFT] or key[K_a]:
        direction = [-SPEED, 0]
    elif key[K_RIGHT] or key[K_d]:
        direction = [SPEED, 0]
    
    snake.move_ip(direction)
    if snake.bottom > WINDOWS_SIZE[1] or snake.top < 0 or snake.left < 0 or snake.right > WINDOWS_SIZE[0]:
        exit_from_game()

    return direction
    
def exit_from_game():
    pygame.quit()
    exit()


if __name__ == "__main__":
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    clock = pygame.time.Clock()
    
    head_image, head_rect = load_img('./ls14/img/head.png', *SPAWN_COORDINATE)
    
    while True: 
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_from_game()
        
        DIRECTION = move(head_rect, DIRECTION)

        screen.blit(head_image, head_rect)
        pygame.display.update()
        clock.tick(10)