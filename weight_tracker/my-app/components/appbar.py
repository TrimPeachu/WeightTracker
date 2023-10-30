import flet as ft


def get_app_bar(page: ft.Page):
    return ft.AppBar(
        title=ft.Text("Weight Tracker"),
        center_title=True,
        actions=[
            ft.IconButton(ft.icons.LOGOUT, on_click=lambda e: page.go("/")),
        ],
    )
