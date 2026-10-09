import pygame, os
from Buttons_Class import Buttons
import Validation3 as validation
import Animation7 as animation


pygame.init()

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 625

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

gamePaused = True  
menuState = "main" 
volume = 0.0
showInfo = False 

defineFont = "verdana"  
titleFont = 'georgia'
displayFont = 'comicsans'  
font = pygame.font.SysFont(titleFont, 40, bold=True) 
fontTwo = pygame.font.SysFont(defineFont, 36, bold=True) 
fontThree = pygame.font.SysFont(displayFont, 36, bold=True)

TEXT_COL = (255, 255, 255) #White
INFO_COL = (0, 255, 0) #Green
CONTROLS_COL = (0, 255, 255) #Cyan

#import images
startImg = pygame.image.load("Buttons/StartButton.png").convert_alpha()  
optionsImg = pygame.image.load("Buttons/OptionsButton.png").convert_alpha()  
exitImg = pygame.image.load("Buttons/ExitButton.png").convert_alpha()  
audioImg = pygame.image.load("Buttons/AudioButton.png").convert_alpha()  
infoImg = pygame.image.load("Buttons/InfoButton.png").convert_alpha()  
returnImg = pygame.image.load("Buttons/ReturnButton.png").convert_alpha()  

startButton = Buttons(475, 50, startImg, 0.5)  
optionsButton = Buttons(475, 250, optionsImg, 0.5)  
exitButton = Buttons(475, 450, exitImg, 0.5) 
audioButton = Buttons(125, 50, audioImg, 0.6)  
infoButton = Buttons(125, 250, infoImg, 0.6)  
returnButton = Buttons(125, 450, returnImg, 0.6)  

#music faetures
pygame.mixer.init()  
pygame.mixer.music.load(os.path.join('Soundtracks', 'Life Soundtrack.mp3'))
pygame.mixer.music.set_volume(volume) 
pygame.mixer.music.play(-1)

#adjust volume
def adjust_volume(increment):
    global volume
    volume = max(0.0, min(1.0, volume + increment))  
    pygame.mixer.music.set_volume(volume) 
    print(f"Volume adjusted to: {volume * 100:.0f}%")  

#render text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)  
    screen.blit(img, (x, y)) 

if validation.logged_in:
    run = True
else:
    run = False
while run:
    screen.fill((52, 78, 91)) 

    if gamePaused: 
        if menuState == "main": 
            if startButton.draw(screen):
                gamePaused = False 
            if optionsButton.draw(screen): 
                menuState = "options"
            if exitButton.draw(screen): 
                run = False

        elif menuState == "options":
            if audioButton.draw(screen): 
                adjust_volume(0.1)
            if infoButton.draw(screen): 
                showInfo = not showInfo 
            if returnButton.draw(screen): 
                menuState = "main"

        if showInfo:
            screen.fill((52, 78, 91))
            draw_text("GAME CONTROLS", fontThree, INFO_COL, 430, 50)
            draw_text("D: Move right", fontTwo, CONTROLS_COL, 50, 200)
            draw_text("A: Move Left", fontTwo, CONTROLS_COL, 50, 300) 
            draw_text("W / Spacebar: Jump", fontTwo, CONTROLS_COL, 50, 400)
            draw_text("Esc: Pause", fontTwo, CONTROLS_COL, 50, 500)
            
    else:
        animation.main()
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                gamePaused = True
        if event.type == pygame.QUIT: 
            run = False  

    pygame.display.update()

pygame.quit()