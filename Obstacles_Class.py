import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
