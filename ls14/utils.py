from variables import DEFAULT_OBJ_SIZE, WINDOWS_SIZE
import pygame

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, DEFAULT_OBJ_SIZE)
    rect = image.get_rect(center=(x, y))
    transpet = image.get_at((0, 0))
    image.set_colorkey(transpet)

    return image, rect

def exit_from_game():
    pygame.quit()
    exit()

def is_out_field(head):
    if head.bottom > WINDOWS_SIZE[1] or head.top < 0 or head.left < 0 or head.right > WINDOWS_SIZE[0]:
        return True
    return False