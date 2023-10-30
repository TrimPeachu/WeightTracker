import flet as ft
from flet import TemplateRoute

from components.appbar import get_app_bar
from components.navbar import NavBar
from views.homepage import PersonalInfo


def profile_page(page: ft.Page, params, basket):
    user_id = params.user_id
    navbar = NavBar(page, user_id).get_navbar()
    navbar.selected_index = 2

    personal_info = PersonalInfo(user_id)

    def update_user():
        personal_info.weight_goal = weight_goal_input.value
        personal_info.height = height_input.value
        personal_info.age = age_input.value
        personal_info.update_user()

    weight_goal_input = ft.TextField(width=100, value=personal_info.weight_goal)
    height_input = ft.TextField(width=100, value=personal_info.height)
    age_input = ft.TextField(width=100, value=personal_info.age)

    return ft.View(
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                        ft.Icon(
                            scale=ft.Scale(4),
                            name='person',
                            animate_scale=ft.Animation(900, "decelerate"),
                        ),
                        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(personal_info.name, size=20, weight=ft.FontWeight.BOLD)
                            ]
                        ),
                        ft.Divider(height=30, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text("Weight Goal"),
                                        weight_goal_input
                                    ]
                                ),
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text("Height"),
                                        height_input
                                    ]
                                ),
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text("Age"),
                                        age_input
                                    ]
                                ),
                            ]
                        ),
                        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    text="SUBMIT",
                                    on_click=lambda e: update_user()
                                )
                            ]
                        ),

                    ]
                ),
                get_app_bar(page),
                navbar
            ]
        )
