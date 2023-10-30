import flet as ft

LOGIN_ICON = "lock"

LOGIN_IMAGE = ft.Icon(
    scale=ft.Scale(4),
    name=LOGIN_ICON,
    animate_scale=ft.Animation(900, "decelerate"),
)

LOGIN_INTRO = "Welcome to Weight Tracker! \n\t\t Please login to continue.",


def get_login_controls(username, password, footer, page_type, authorize_user, routing):
    return [
        ft.SafeArea(
            minimum=5,
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment="center",
                        controls=[
                            LOGIN_IMAGE
                        ],
                        height=200
                    ),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Text(
                                LOGIN_INTRO,
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
                                    password
                                ],
                            )
                        ],
                    ),
                    ft.Divider(height=10, color='transparent'),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.ElevatedButton(
                                text=page_type,
                                on_click=lambda e: authorize_user(),
                            ),
                        ],
                    ),
                    ft.Divider(height=120, color='transparent'),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Text(
                                footer,
                                spans=[
                                    ft.TextSpan(
                                        text=" here!",
                                        style=ft.TextStyle(italic=True),
                                        on_click=lambda e: routing()
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            ),
        ),
    ]

