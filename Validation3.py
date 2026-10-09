import flet as ft 
import pygame
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

username = None
password = None

logged_in = False

def login(page: ft.Page) -> None:
    page.title = "Sign In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1250
    page.window_height = 625
    page.window_resisable = True

    title_text = 'Welcome to Rapid Runner!'
    title_display =  ft.Text(title_text, theme_style=ft.TextThemeStyle.TITLE_LARGE, font_family= "georgia")

    #text field instantiation 
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='I am not a robot', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign in', width=200, disabled=True)
    error_message_display: Text = Text(value="", color="red")
    close_button = ft.ElevatedButton("Close Game", on_click=lambda e: page.window_destroy())

    #validation complete (checkoc complete)
    def input_validation(e) -> None:
        #make conditions pop up one by one (complete)
        if len(text_username.value) < 5:
            error_message_display.value = ("Username must be at least 5 characters long.")
            button_submit.disabled = True
        elif len(text_password.value) < 8:
            error_message_display.value = ("Password must be at least 8 characters long.")
            button_submit.disabled = True
        elif not any(char.isdigit() for char in text_password.value):
            error_message_display.value = ("Password must contain at least one number.")
            button_submit.disabled = True
        elif not checkbox_signup.value:
            error_message_display.value = ("Please confirm that you are not a robot.")
            button_submit.disabled = True
        else:
            error_message_display.value = ""
            button_submit.disabled = False
        page.update()

    def submit(e) -> None:
        global username, password, logged_in
        print(f'Username: {text_username.value}')
        print(f'Password: {text_password.value}')
        username = text_username.value
        password = text_password.value

        logged_in = True

        #clear page
        page.clean()
        page.add(
            Row(
                controls=[
                    Text(value=f"Welcome {text_username.value}!", size=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    #links functions to UI
    checkbox_signup.on_change = input_validation
    text_username.on_change = input_validation
    text_password.on_change = input_validation
    button_submit.on_click = submit    

    #adds feilds to the screen
    page.add(
        Row(
            controls=[
                Column(
                    [title_display,
                    text_username,
                    text_password,
                    checkbox_signup,
                    button_submit,
                    error_message_display]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=login)

#saves user info
file = open('name_password.txt', 'a')
file.write(f"\n{username} : {password}")
