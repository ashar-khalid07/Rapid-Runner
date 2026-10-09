import pygame
import random

screenWidth = 1250
screenHeight = 650

class Obstacle(pygame.sprite.Sprite):
    #define my key variables
    def __init__(self, x, y, width, height, colour, speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        #Obstcale moves <-
        self.rect.x -= self.speed

        #Takes obstacle when off-screen
        if self.rect.right < 0:
            self.kill()

