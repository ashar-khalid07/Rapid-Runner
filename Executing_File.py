from pathlib import Path
import os
import pygame

from Buttons_Class import Buttons
import Animation7 as animation

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 625
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rapid Runner")

TEXT_COL = (255, 255, 255)
INFO_COL = (0, 255, 0)
CONTROLS_COL = (0, 255, 255)

font = pygame.font.SysFont("georgia", 40, bold=True)
font_two = pygame.font.SysFont("verdana", 36, bold=True)
font_three = pygame.font.SysFont("comicsans", 36, bold=True)

start_img = pygame.image.load("Buttons/StartButton.png").convert_alpha()
options_img = pygame.image.load("Buttons/OptionsButton.png").convert_alpha()
exit_img = pygame.image.load("Buttons/ExitButton.png").convert_alpha()
audio_img = pygame.image.load("Buttons/AudioButton.png").convert_alpha()
info_img = pygame.image.load("Buttons/InfoButton.png").convert_alpha()
return_img = pygame.image.load("Buttons/ReturnButton.png").convert_alpha()

start_button = Buttons(475, 50, start_img, 0.5)
options_button = Buttons(475, 250, options_img, 0.5)
exit_button = Buttons(475, 450, exit_img, 0.5)
audio_button = Buttons(125, 50, audio_img, 0.6)
info_button = Buttons(125, 250, info_img, 0.6)
return_button = Buttons(125, 450, return_img, 0.6)

volume = 0.0
audio_available = False

def start_menu_music() -> None:
    global audio_available
    soundtrack = BASE_DIR / "Soundtracks" / "Life Soundtrack.mp3"
    if not soundtrack.exists():
        audio_available = False
        return
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        audio_available = True
    except pygame.error:
        audio_available = False

def adjust_volume(increment: float) -> None:
    global volume
    volume = max(0.0, min(1.0, volume + increment))
    if audio_available:
        pygame.mixer.music.set_volume(volume)

def draw_text(text, selected_font, colour, x, y) -> None:
    screen.blit(selected_font.render(text, True, colour), (x, y))

def main() -> None:
    global volume
    game_paused = True
    menu_state = "main"
    show_info = False
    run = True
    start_menu_music()

    while run:
        screen.fill((52, 78, 91))

        if game_paused:
            if menu_state == "main":
                if start_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
                if exit_button.draw(screen):
                    run = False
            elif menu_state == "options":
                if audio_button.draw(screen):
                    adjust_volume(0.1)
                if info_button.draw(screen):
                    show_info = not show_info
                if return_button.draw(screen):
                    menu_state = "main"

            if show_info:
                screen.fill((52, 78, 91))
                draw_text("GAME CONTROLS", font_three, INFO_COL, 430, 50)
                draw_text("D: Move right", font_two, CONTROLS_COL, 50, 200)
                draw_text("A: Move left", font_two, CONTROLS_COL, 50, 300)
                draw_text("W / Spacebar: Jump", font_two, CONTROLS_COL, 50, 400)
                draw_text("Esc: Return to menu", font_two, CONTROLS_COL, 50, 500)
        else:
            return_to_menu = animation.main()
            if not return_to_menu:
                run = False
                continue
            game_paused = True
            menu_state = "main"
            start_menu_music()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
