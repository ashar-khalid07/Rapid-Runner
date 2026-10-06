"""Optional Flet interface retained from the original project work.

This is a player-name setup screen, not an authentication system. It deliberately
stores no credentials and writes no user data to disk.
"""

import flet as ft

def player_setup(page: ft.Page) -> None:
    page.title = "Rapid Runner - Player Setup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    title = ft.Text("Welcome to Rapid Runner!", theme_style=ft.TextThemeStyle.TITLE_LARGE, font_family="georgia")
    player_name = ft.TextField(label="Player name", width=240)
    status = ft.Text(value="", color="red")
    continue_button = ft.ElevatedButton(text="Continue", width=240, disabled=True)

    def validate(_):
        name = (player_name.value or "").strip()
        continue_button.disabled = len(name) < 2
        status.value = "Enter at least two characters." if len(name) < 2 else ""
        page.update()

    def continue_to_game(_):
        name = (player_name.value or "").strip()
        page.clean()
        page.add(ft.Row(controls=[ft.Text(value=f"Ready to run, {name}!", size=42)], alignment=ft.MainAxisAlignment.CENTER))

    player_name.on_change = validate
    continue_button.on_click = continue_to_game

    page.add(ft.Row(controls=[ft.Column([title, player_name, continue_button, status])], alignment=ft.MainAxisAlignment.CENTER))

if __name__ == "__main__":
    ft.app(target=player_setup)
