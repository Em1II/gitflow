import pygame
from axil import load_image
pygame.display.init()
size = 600, 600
height, width = size
screen = pygame.display.set_mode(size)
FPS = 60
pygame.display.set_caption("Десант")
all_sprites = pygame.sprite.Group()

running = True
class Landing(pygame.sprite.Sprite):
    
    image = load_image("pt.png",)
    def __init__(self, pos):
        
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0.0, float(1))
class Mountain(pygame.sprite.Sprite):
    
    image = load_image("mountains.png",)
    def __init__(self):
        
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height
if __name__ == "__main__":
    mountain = Mountain()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
            

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        
        
        pygame.display.flip()
    pygame.quit()