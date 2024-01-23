import flet as ft
import requests


def register_user(page, username, password, weight_goal, height, age):
    url = "http://127.0.0.1:8000/users/create/"
    body = {
        "username": username,
        "password": password,
        "weight_goal": weight_goal,
        "height": height,
        "age": age
    }

    response = requests.post(url, data=body)

    if response.status_code == 200:
        page.go("/login")
    else:
        print("Error")

def register_page(page: ft.Page, params, basket):
    # def login_page(page: ft.Page):
    icon = "person_2_sharp"
    image = ft.Icon(
        scale=ft.Scale(4),
        name=icon,
        animate_scale=ft.Animation(900, "decelerate"),
    )

    username = ft.TextField(width=350)
    passcode = ft.TextField(password=True, width=350)
    weight_goal = ft.TextField(width=110, label="Weight goal", keyboard_type=ft.KeyboardType.NUMBER)
    height = ft.TextField(width=110, label="Height", keyboard_type=ft.KeyboardType.NUMBER)
    age = ft.TextField(width=110, label="Age", keyboard_type=ft.KeyboardType.NUMBER)

    intro = "Welcome to Weight Tracker! \n Please register to continue."
    footer = "Already have an account? \n\t\t\t\t\t\t\t\t\t\t Login"

    return ft.View(
        controls=[
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment="center",
                            controls=[
                                image
                            ],
                            height=200
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    intro,
                                    size=16,
                                    weight='bold',
                                )
                            ],
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text("Username"),
                                        username,
                                        ft.Divider(height=2.5, color='transparent'),
                                        ft.Text("Password"),
                                        passcode,
                                        ft.Divider(height=2.5, color='transparent'),
                                        ft.Row(
                                            controls=[
                                                weight_goal,
                                                height,
                                                age
                                            ]

                                        )
                                    ],
                                )
                            ],
                        ),
                        ft.Divider(height=10, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.ElevatedButton(
                                    text="REGISTER",
                                    on_click=lambda e: register_user(page, username.value, passcode.value, weight_goal.value, height.value, age.value)
                                )
                            ]
                        ),
                        # ft.Divider(height=120, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    footer,
                                    spans=[
                                        ft.TextSpan(
                                            text=" here!",
                                            style=ft.TextStyle(italic=True),
                                            on_click=lambda e: page.go("/login")
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )
