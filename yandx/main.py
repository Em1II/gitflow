import os
import sys

import pygame
from axil import load_image






if __name__ == "__main__":
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    FPS = 60
    pygame.display.set_caption("Герой движется")
    running = True
    all_sprites = pygame.sprite.Group()
    hero_img = load_image('creature.png')
    hero = pygame.sprite.Sprite(all_sprites)
    hero.image = hero_img
    hero.rect = hero.image.get_rect()
    speed = 10
    clock = pygame.time.Clock()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            hero.rect.top += speed
        if keys[pygame.K_UP]:
            hero.rect.top -= speed
        if keys[pygame.K_LEFT]:
            hero.rect.left -= speed
        if keys[pygame.K_RIGHT]:
            hero.rect.right += speed
        
            
            
                

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
