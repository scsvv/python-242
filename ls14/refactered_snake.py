import pygame
from variables import * 
from utils import load_img, exit_from_game, is_out_field
from random import randint


def move(snake, direction):
    key = pygame.key.get_pressed()

    if (key[K_UP] or key[K_w]) and direction[0]: 
        direction = [0, -SPEED]
    elif (key[K_DOWN] or key[K_s]) and direction[0]:
        direction = [0, SPEED]
    elif (key[K_LEFT] or key[K_a]) and direction[1]:
        direction = [-SPEED, 0]
    elif (key[K_RIGHT] or key[K_d]) and direction[1]:
        direction = [SPEED, 0]
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y
    snake[0].move_ip(direction)

    if is_out_field(snake[0]):
        exit_from_game()

    return direction

def pickup(apple, snake):
    global SCORE
    if snake[0].colliderect(apple):
        apple.x = randint(10, 1050)
        apple.y = randint(10, 670)
        
        snake.append(snake[1].copy())
        
        SCORE += 10

def display_score(score = 0):
    text = font.render(f"Score: {score}", True, WHITE)
    text_rect = text.get_rect(left=5, top=5)
    screen.blit(text, text_rect)


def game_procces(snake, apple, score, direction):
    direction = move(snake, direction)
    pickup(apple, snake)
    display_score(score)
    return direction

def is_game(snake):
    for shape in snake[1:]:
        if snake[0].colliderect(shape):
            return False
    return True 


if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 16)

    head_image, head_rect = load_img('./ls14/img/head.png', *SPAWN_COORDINATE)
    body_image, body_rect = load_img('./ls14/img/body.png', *BODY_SPAWN_COORDINATE)
    apple_imaage,apple_rect = load_img('./ls14/img/apple.png', *APPLE_SPAWN_COORDINATE)

    snake = [head_rect, body_rect]

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_from_game()
    

        if is_game(snake):
            DIRECTION = game_procces(snake, apple_rect, SCORE, DIRECTION)

            screen.blit(head_image, head_rect)
            screen.blit(apple_imaage, apple_rect)
            for body in snake[1:]:
                screen.blit(body_image, body)
        else:
            exit_from_game()

        pygame.display.update()
        clock.tick(10)            

