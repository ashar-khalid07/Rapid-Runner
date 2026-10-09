import pygame

pygame.init()

#game window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

healthScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Health Bar')

class Health():
  def __init__(self, x, y, w, h, max_hp): #leftright of bar, up bar, down bar, vol of bar, length of bar
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    #calculate health ratio
    ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

healthBar = Health(10, 50, 220, 40, 96)

run = False

if __name__ == "__main__":
  run = True
while run:

  healthScreen.fill('indigo')
  #draw health bar
  healthBar.hp = 100
  healthBar.draw(healthScreen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()