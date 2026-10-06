from pathlib import Path
import math
import os
import random
import pygame

from HealthBar import Health
from Obstacles_Class import Obstacle

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()

clock = pygame.time.Clock()
FPS = 60
screenWidth = 1250
screenHeight = 625
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Rapid Runner")

xPos, yPos = 70, 450

red = (255, 0, 0)
navy = (0, 0, 128)
orange = (255, 165, 0)
purple = (128, 0, 128)
maroon = (115, 0, 0)
forestGreen = (0, 50, 0)
highlighter = (255, 255, 100)
lime = (180, 255, 100)
obstacleColours = [red, navy, orange, purple, maroon, forestGreen, lime, highlighter]

mainFont = pygame.font.Font(None, 36)
INCREMENT_SCORE = pygame.USEREVENT + 1
pygame.time.set_timer(INCREMENT_SCORE, 2000)

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.sprites = []
        self.jumpSprites = []
        self.isAnimating = True
        self.jump = False
        self.speed = 5

        for image in range(1, 9):
            runImg = pygame.transform.scale(pygame.image.load(os.path.join("Run_Animation", f"run{image}.png")), (100, 100))
            self.sprites.append(runImg)

        for image in range(1, 9):
            jumpImg = pygame.transform.scale(pygame.image.load(os.path.join("Jump_Animation", f"jump{image}.png")), (100, 100))
            self.jumpSprites.append(jumpImg)

        self.frameIndex = 0
        self.jumpFrame = 0
        self.gravity = 1
        self.jumpHeight = 22
        self.yVelocity = self.jumpHeight
        self.pos = [posX, posY]
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump = True
        if self.jump:
            self.pos[1] -= self.yVelocity
            self.yVelocity -= self.gravity
            if self.yVelocity < -self.jumpHeight:
                self.jump = False
                self.yVelocity = self.jumpHeight
        if keys[pygame.K_a]:
            self.pos[0] -= self.speed
        if keys[pygame.K_d]:
            self.pos[0] += self.speed
        self.pos[0] = max(0, min(self.pos[0], screenWidth - self.rect.width))

    def update(self):
        if self.isAnimating and not self.jump:
            self.currentSprite += 0.3
            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
        if self.jump:
            self.jumpFrame += 0.25
            if self.jumpFrame >= len(self.jumpSprites):
                self.jumpFrame = 0
            self.image = self.jumpSprites[int(self.jumpFrame)]
        else:
            self.image = self.sprites[int(self.currentSprite)]
        self.move()
        self.rect.topleft = self.pos
        self.draw()

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

def draw_score(score):
    scoreText = mainFont.render(f"Score: {score}", True, orange)
    screen.blit(scoreText, (10, 10))

def start_game_music():
    soundtrack = BASE_DIR / "Soundtracks" / "Sky Soundtrack.mp3"
    if not soundtrack.exists():
        return False
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        return True
    except pygame.error:
        return False

def main():
    run = True
    return_to_menu = True
    score = 0
    pygame.time.set_timer(INCREMENT_SCORE, 2000)
    latestTime = pygame.time.get_ticks()
    timeInterval = 7500
    obstacleInterval = pygame.time.get_ticks() + random.randint(500, 1800)

    bg = pygame.transform.scale(pygame.image.load(os.path.join("Game_Backgrounds", "darkcity.jpeg")), (screenWidth, screenHeight))
    bgWidth = bg.get_width()
    scroll = 0
    bgSpeed = 7.5
    tiles = math.ceil(screenWidth / bgWidth) + 1

    player = Player(xPos, yPos)
    obstacles = pygame.sprite.Group()
    healthbar = Health(1035, 10, 200, 30, 100)
    audio_started = start_game_music()

    while run:
        clock.tick(FPS)
        currentTime = pygame.time.get_ticks()
        if currentTime - latestTime >= timeInterval:
            bgSpeed = min(22, bgSpeed + 0.9)
            latestTime = currentTime

        for i in range(tiles):
            screen.blit(bg, (i * bgWidth + scroll, 0))
        scroll -= bgSpeed
        if abs(scroll) > bgWidth:
            scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return_to_menu = False
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            elif event.type == INCREMENT_SCORE:
                score += 50

        if currentTime >= obstacleInterval:
            heightObs = random.randint(40, 80)
            widthObs = random.randint(50, 200)
            yPlacement = random.randint(screenHeight - 200, screenHeight - heightObs - 70)
            colour = random.choice(obstacleColours)
            obstacle = Obstacle(screenWidth, yPlacement, widthObs, heightObs, colour, int(bgSpeed))
            obstacleInterval = currentTime + random.randint(700, 1800)
            obstacles.add(obstacle)

        player.update()
        obstacles.update()
        obstacles.draw(screen)
        draw_score(score)
        healthbar.draw(screen)

        hit = pygame.sprite.spritecollideany(player, obstacles)
        if hit:
            healthbar.hp -= 33.4
            hit.kill()

        if healthbar.hp <= 0:
            print(f"Game over. Final score: {score}")
            run = False

        pygame.display.update()

    if audio_started:
        pygame.mixer.music.stop()
    return return_to_menu

if __name__ == "__main__":
    main()
