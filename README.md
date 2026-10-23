# Rapid Runner

Rapid Runner is an endless-runner game I built in Python for coursework between November 2024 and April 2025. I developed the whole program myself, including the Flet sign-in screen, the Pygame main menu and the animated game screen.

## Why I built it

The project was part of my coursework and gave me the chance to build a larger program made up of several files, classes and features rather than one small script.

I wanted the different parts of the program to work together as one complete flow: sign in, open the menu and then start the game.

## What I built

The project has three main parts:

- a Flet sign-in screen with basic input validation
- a Pygame main menu with start, options and controls screens
- the endless-runner game itself, including animation, movement, obstacles, scoring, health and collision handling

I programmed all of these parts myself.

## Main functionality

- Sign-in form built with Flet
- Main menu with start, options and controls screens
- Running and jumping sprite animations
- Left and right movement
- Scrolling background that gradually increases in speed
- Randomly generated obstacles
- Collision detection and a health bar
- Score tracking
- Audio controls in the menu

## Technologies

- Python
- Pygame
- Flet

## The main challenge

The animation/game section was the most difficult part of the project.

The challenge was not one individual feature. It was getting several classes, files and game systems to work together without breaking each other. The player animation, movement, obstacles, health, collisions, score, background scrolling and menu all had to work as part of the same program.

Working through those integration problems was one of the main parts of the project and helped me become more comfortable debugging a program spread across multiple Python files.

## What I learned

Rapid Runner was where I gained most of my early practical experience with Pygame and Flet.

Through building it, I became more comfortable with:

- Pygame's game loop and event system
- sprite animation and movement
- classes and objects across multiple files
- collision detection
- timing and score updates
- handling user input
- building interfaces with Flet
- combining separate parts of a program into one working application
- debugging issues caused by interactions between different files and features

## How to run it

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python Executing_File.py
```

The original project expects soundtrack files inside a `Soundtracks/` folder. Those audio files are not included in this public repository because I do not have clear licensing information for them. As a result, the original program will need suitable local/replacement audio files before it can run exactly as written.

## Project structure

```text
Executing_File.py        Main menu and application entry point
Validation3.py           Flet sign-in screen
Animation7.py            Main game loop and player animation
Buttons_Class.py         Reusable menu button class
Obstacles_Class.py       Obstacle sprite class
HealthBar.py             Health bar
Buttons/                 Menu button images
Run_Animation/           Running animation frames
Jump_Animation/          Jumping animation frames
Game_Backgrounds/        Game background
```

## Current limitations

This repository contains the original coursework code, including some decisions I would change now.

The sign-in screen prints the entered username/password and writes them to `name_password.txt` in plain text. It should therefore only be treated as a coursework prototype and should never be used with real credentials.

There are also areas of the game loop and restart/pause behaviour that could be improved if I continued developing the project.

## Possible next steps

- Remove plaintext password storage
- Replace the prototype sign-in with proper authentication or remove it
- Improve the game restart and pause behaviour
- Improve obstacle spawning
- Add automated tests for non-graphical logic
- Replace the omitted soundtrack files with clearly licensed audio
