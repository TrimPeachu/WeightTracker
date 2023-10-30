import flet as ft
import requests


def authorize_user(page, username, password):
    url = f"http://127.0.0.1:8000/login/{username}/{password}/"

    response = requests.get(url)

    if response.status_code == 200:
        id = response.json()["id"]
        print(f"User {id} authorized")
        print(f"Redirecting to /home/{id}")
        print(f"Response: {response.json()}")
        page.go(f"/home/{id}")
        page.update()
    else:
        dlg = ft.AlertDialog(
            title=ft.Text(
                "Incorrect username or password",
                color="red"
            ),
            on_dismiss=lambda e: print("Dismissed"),
        )

        page.dialog = dlg
        dlg.open = True
        page.update()


def login_page(page: ft.Page, params, basket):
# def login_page(page: ft.Page):
    icon = "lock"
    image = ft.Icon(
        scale=ft.Scale(4),
        name=icon,
        animate_scale=ft.Animation(900, "decelerate"),
    )

    username = ft.TextField(width=350)
    passcode = ft.TextField(password=True, width=350)

    intro = "Welcome to the Weight Tracker! \n\t\t Please login to continue."
    footer = "Don't have an account? \n\t\t\t\t\t\t\t Register"

    return ft.View(
        "/",
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
                        ft.Divider(height=40, color='transparent'),
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
                                    ],
                                )
                            ],
                        ),
                        ft.Divider(height=10, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.ElevatedButton(
                                    text="LOGIN",
                                    on_click=lambda e: authorize_user(page, username.value, passcode.value)
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
                                            on_click=lambda e: page.go("/register")
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
