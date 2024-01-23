import flet as ft


class NavBar:
    def __init__(self, page: ft.Page, user_id: int):
        self.page = page
        self.user_id = user_id

        self.navbar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME, label="HOME"),
                ft.NavigationDestination(icon=ft.icons.TABLE_ROWS, label="DATA"),
                ft.NavigationDestination(icon=ft.icons.PERSON, label="PROFILE"),
            ],
            on_change=lambda e: self.change_page(e),
        )

    def change_page(self, e):
        if e.data == '0':
            self.page.go(f"/home/{self.user_id}")
        elif e.data == '1':
            self.page.go(f"/data/{self.user_id}")
        elif e.data == '2':
            self.page.go(f"/profile/{self.user_id}")
        else:
            print(f"Error \n Data provided: {e.data}")

    def get_navbar(self):
        return self.navbar

