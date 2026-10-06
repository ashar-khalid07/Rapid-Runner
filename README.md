# Rapid Runner

Rapid Runner is a Python endless-runner prototype built with Pygame. It includes a menu, animated player movement, a scrolling background, random obstacles, scoring, health and an optional Flet interface prototype.

## Features

- Pygame main menu with start, options and controls views
- Animated running and jumping sprites
- Left/right movement plus jump controls
- Scrolling background with gradually increasing speed
- Randomised obstacle sizes, positions, colours and spawn intervals
- Collision-based health reduction and game-over condition
- Score increments over time
- Optional Flet player-name interface prototype
- Optional audio hooks when local soundtrack assets are present

## Technologies

- Python
- Pygame
- Flet

## Screenshots

No generated or mock screenshot is included. Run the application locally to view the current game.

## Getting Started

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python Executing_File.py
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python Executing_File.py
```

Controls in the game are **A/D** to move, **W** or **Space** to jump, and **Esc** to return to the menu.

The optional Flet interface can be run separately with:

```bash
python Flet_Interface.py
```

It is a player-name UI prototype, not an authentication system.

## Project Structure

```text
Executing_File.py        Main Pygame menu and application entry point
Animation7.py            Runner game loop, player animation, scoring and collisions
Buttons_Class.py         Reusable image-button component
Obstacles_Class.py       Moving obstacle sprite
HealthBar.py             Health-bar rendering
Flet_Interface.py        Optional non-authentication Flet UI prototype
Buttons/                 Menu button images
Run_Animation/           Running sprite frames
Jump_Animation/          Jumping sprite frames
Game_Backgrounds/        Game background asset
```

## Testing

No automated test suite is included. The Python source was syntax-checked during portfolio preparation. Full runtime verification requires Pygame/Flet and a graphical environment.

## Security / Portfolio Cleanup

The supplied project archive contained an older Flet sign-in prototype that printed usernames/passwords and appended them to a plaintext `name_password.txt` file. That behaviour has been removed from the public portfolio version. The retained Flet component requests only a player name, stores no credentials and is not presented as authentication.

The two original soundtrack files are not published because their licensing/provenance is not documented. The code now treats audio as optional, so the game still runs without them.

Unused coursework/prototype files were also excluded so the repository focuses on the final game path and the assets it uses.

## What I Worked On

This was an individual project. My work represented here includes the Pygame menu, player movement and animation, scrolling game loop, obstacle generation, health/collision logic, scoring and the supporting Flet interface work.

## Further Improvements

Potential future improvements include a dedicated game-over screen, separating game state from rendering for easier testing, automated tests for non-graphical logic, improved pause/restart flow and clearer provenance/licensing documentation for media assets.
