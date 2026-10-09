import pygame, sys, os, math, random 
from HealthBar import Health
from Obstacles_Class import Obstacle
pygame.init()

clock = pygame.time.Clock()
FPS = 60

temp = 0

#the game screen
screenWidth = 1250
screenHeight = 625
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Rapid Runner")

#init pos of my character
xPos, yPos = 70, 450

#all obstacle colours
red = (255, 0, 0)
navy = (0, 0, 128)
orange = (255, 165, 0)
purple = (128, 0, 128)
marroon = (115,0,0)
forestGreen = (0,50,0)
highlighter = (255,255,100)
lime = (180,255,100)
obstacleColours = [red, navy, orange, purple, marroon, forestGreen, lime, highlighter ]

#the score font
mainFont = pygame.font.Font(None, 36)

#sprite groups
allSprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

#defining the healthbar (put top right)
healthbar = Health(1035, 10, 200, 30, 100)


class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        #groups and key variables
        self.sprites = []
        self.jumpSprites = []
        self.isAnimating = True
        self.jump = False
        self.speed = 5

        #my character run loop
        for image in range(1, 9):
            runImg = pygame.transform.scale(pygame.image.load(os.path.join('Run_Animation', f'run{image}.png')), (100, 100))
            self.sprites.append(runImg)

        #character jump loop
        for i in range(1, 9):
            jumpImg = pygame.transform.scale(pygame.image.load(os.path.join('Jump_Animation', f'jump{i}.png')), (100, 100))
            self.jumpSprites.append(jumpImg)

        #jumping mechanics
        self.frameIndex = 0
        self.jumpFrame = 0
        self.gravity = 1
        self.jumpHeight = 22
        self.yVelocity = self.jumpHeight
        self.pos = [posX, posY]

        #character positioning
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]

    #movement of character
    def move(self):
        #input A and D and spacebar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump = True

        #jump condition
        if self.jump:
            self.pos[1] -= self.yVelocity
            self.yVelocity -= self.gravity
            if self.yVelocity < -self.jumpHeight:
                self.jump = False
                self.yVelocity = self.jumpHeight
        
        #move left or right
        if keys[pygame.K_a]:
            self.pos[0] -= self.speed
        if keys[pygame.K_d]:
            self.pos[0] += self.speed

    #updates character features all the time
    def update(self):
        if self.isAnimating and not self.jump:
            self.currentSprite += 0.3
            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
        
        #jump condition 2
        if self.jump:
            self.jumpFrame += 0.25
            if self.jumpFrame >= len(self.jumpSprites):
                self.jumpFrame = 0

        #jump condition 3
        if self.jump:
            self.image = self.jumpSprites[int(self.jumpFrame)]
        else:
            self.image = self.sprites[int(self.currentSprite)]

        self.move()
        self.rect.topleft = self.pos
        self.draw()

    #this draws character 
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#score display
def draw_score(score):
    scoreText = mainFont.render(f"Score: {score}", True, orange)
    screen.blit(scoreText, (10, 10))



#key variable for score and obstacles
INCREMENT_SCORE = pygame.USEREVENT + 1
pygame.time.set_timer(INCREMENT_SCORE, 2000)

#music
volume = 0.5
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('Soundtracks', 'Sky Soundtrack.mp3'))
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

#main game loop

#run = True
def main():
    run = True
    score = 0

    #time variables
    latestTime = pygame.time.get_ticks()
    timeInterval = 7500
    ObstacleInterval = pygame.time.get_ticks() + random.randint(500, 1800)

    #loads the bg
    bg = pygame.transform.scale(pygame.image.load(os.path.join('Game_Backgrounds', 'darkcity.jpeg')), (screenWidth, screenHeight))
    bgWidth = bg.get_width()
    bgRect = bg.get_rect()

    #game variables associated with bg
    scroll = 0
    BgInitSpeed = 7.5
    tiles = math.ceil(screenWidth / bgWidth) + 1
    
    #craetes player
    player = Player(xPos, yPos)
    allSprites.add(player)
    movingSprites = pygame.sprite.Group()
    movingSprites.add(player)

    while run:
        clock.tick(FPS)
        currentTime = pygame.time.get_ticks()

        #bg speed
        if currentTime - latestTime >= timeInterval:
            BgInitSpeed += 0.9
            if BgInitSpeed > 22:
                BgInitSpeed = 22
            latestTime = currentTime

        #draw bg
        for i in range(tiles):
            screen.blit(bg, (i * bgWidth + scroll, 0))
        scroll -= BgInitSpeed
        if abs(scroll) > bgWidth:
            scroll = 0

        #event handling COME BACK LATER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == INCREMENT_SCORE:
                score += 50
            if currentTime >= ObstacleInterval:
                heightObs = random.randint(40, 80)
                widthObs = random.randint(50, 200)
                yPlacement = random.randint(screenHeight - 200, screenHeight - heightObs - 70)
                colour = random.choice(obstacleColours)
                speed = int(BgInitSpeed)
                obstacle = Obstacle(screenWidth, yPlacement, widthObs, heightObs, colour, speed)
                ObstacleInterval = currentTime + random.randint(700, 1800)
                allSprites.add(obstacle)
                obstacles.add(obstacle)

        #update sprites
        player.update()
        obstacles.update()

        #draw my obstacles and score and healthbar
        obstacles.draw(screen)
        draw_score(score)
        healthbar.draw(screen)

        #colision condition
        hit = pygame.sprite.spritecollideany(player, obstacles)
        if hit:
            healthbar.hp -= 33.4
            hit.kill()

        #healthbar condition
        if healthbar.hp <= 0:
            print("Game Over!")
            run = False

        pygame.display.update()


if __name__ == "__main__":
    main()

################ADDED RANDOM INTERVALS, ANIMATION DISPLAY COMPLETE
