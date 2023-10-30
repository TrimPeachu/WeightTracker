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
                # ft.NavigationDestination(icon=ft.icons.SETTINGS, label="SETTINGS"),
            ],
            on_change=lambda e: self.change_page(e),
            # selected_index=0
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


# def get_nav_bar(page: ft.Page, user_id: int):
#     return ft.NavigationBar(
#         destinations=[
#             ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="HOME"),
#             ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINED, selected_icon=ft.icons.PERSON, label="PROFILE"),
#             ft.NavigationDestination(icon=ft.icons.TABLE_ROWS_OUTLINED, selected_icon=ft.icons.TABLE_ROWS, label="DATA"),
#             # ft.NavigationDestination(icon=ft.icons.SETTINGS, label="SETTINGS"),
#         ],
#         on_change=lambda e: change_page(page, e, user_id),
#         # selected_index=0
#     )
#
#
# def change_page(page: ft.Page, e, user_id: int):
#     if e.data == '0':
#         page.route = f"/home/{user_id}"
#     elif e.data == '1':
#         page.route = f"/profile/{user_id}"
#     elif e.data == '2':
#         page.route = f"/data/{user_id}"
#     else:
#         print(f"Error \n Data provided: {e.data}")
