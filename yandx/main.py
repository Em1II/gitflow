import os
import sys

import pygame

# Изображение не получится загрузить 
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print(message)
        raise SystemExit(message)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image



if __name__ == "__main__":
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)
    FPS = 60
    pygame.display.set_caption("Курсор")
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    pygame.mouse.set_visible(False)
    # создадим спрайт
    cursor_img = load_image("arrow.png")
    # определим его вид
    cursor = pygame.sprite.Sprite(all_sprites)
    # и размеры
    cursor.image = cursor_img
    cursor.rect = cursor.image.get_rect()
    running = True
    # добавим спрайт в группу
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            
                

        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
