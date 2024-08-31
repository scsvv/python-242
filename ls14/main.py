import pygame
from variables import * 
from sys import exit
from random import randint

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

    if (key[K_UP] or key[K_w]) and direction[0]: 
        direction = [0, -SPEED]
    elif (key[K_DOWN] or key[K_s]) and direction[0]:
        direction = [0, SPEED]
    elif (key[K_LEFT] or key[K_a]) and direction[1] :
        direction = [-SPEED, 0]
    elif (key[K_RIGHT] or key[K_d]) and direction[1]:
        direction = [SPEED, 0]
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y
    snake[0].move_ip(direction)

    if snake[0].bottom > WINDOWS_SIZE[1] or snake[0].top < 0 or snake[0].left < 0 or snake[0].right > WINDOWS_SIZE[0]:
        exit_from_game()

    return direction
    
def exit_from_game():
    pygame.quit()
    exit()

def display_score(score = 0):
    text = font.render(f"Score: {score}", True, WHITE)
    text_rect = text.get_rect(left=5, top=5)
    screen.blit(text, text_rect)

def pickup(apple, snake):
    global SCORE
    if snake[0].colliderect(apple):
        apple.x = randint(10, 1050)
        apple.y = randint(10, 670)
        
        snake.append(snake[1].copy())
        
        SCORE += 10

def is_game(snake):
    for shape in snake[1:]:
        if snake[0].colliderect(shape):
            return False
        return True 


if __name__ == "__main__":
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 16)
    head_image, head_rect = load_img('./ls14/img/head.png', *SPAWN_COORDINATE)
    body_image, body_rect = load_img('./ls14/img/body.png', *BODY_SPAWN_COORDINATE)
    apple_imaage,apple_rect = load_img('./ls14/img/apple.png', *APPLE_SPAWN_COORDINATE)

    snake = [head_rect, body_rect]

    while is_game(snake): 
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_from_game()
        
        DIRECTION = move(snake, DIRECTION)
        
        screen.blit(head_image, head_rect)
        screen.blit(apple_imaage, apple_rect)

        for body in snake[1:]:
            screen.blit(body_image, body)

        pickup(apple_rect, snake)
        display_score(SCORE)
        pygame.display.update()
        clock.tick(10)