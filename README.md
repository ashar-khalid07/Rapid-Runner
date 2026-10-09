# Rapid Runner

Rapid Runner is a Python endless-runner project I built with Pygame, with a Flet sign-in interface used before the game starts.

## Main functionality

- Main menu with start, options and controls screens
- Animated running and jumping sprites
- Left/right movement and jumping
- Scrolling background that increases in speed
- Random obstacles
- Score tracking
- Health and collision handling
- Flet sign-in form with basic input validation

## Technologies

- Python
- Pygame
- Flet

## How to run it

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python Executing_File.py
```

The original project expects local soundtrack files under `Soundtracks/`. Those audio files are not included in this public repository because I do not have clear licensing information for them, so the game will need replacement/local audio files before the original execution path will run as written.

## Project structure

```text
Executing_File.py        Main menu and application entry point
Validation3.py           Original Flet sign-in interface
Animation7.py            Main runner game loop
Buttons_Class.py         Button component
Obstacles_Class.py       Obstacle sprite
HealthBar.py             Health-bar code
Buttons/                 Menu button images
Run_Animation/           Running frames
Jump_Animation/          Jumping frames
Game_Backgrounds/        Game background
```

## Important security note

This repository preserves the original coursework code. The sign-in prototype prints the entered username/password and appends them to `name_password.txt` in plain text.

It is not a secure authentication system and should never be used with real credentials. This is one of the areas I would change if I continued the project.

## Possible next steps

- Remove plaintext password storage
- Replace the prototype sign-in with proper authentication or remove it
- Improve game restart/pause behaviour
- Fix obstacle spawning so it is not dependent on event handling
- Add automated tests for non-graphical logic
- Replace the omitted soundtrack files with clearly licensed audio
