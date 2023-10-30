import flet as ft
from flet_route import Routing, path

from views.login import login_page
from views.register import register_page
# from views.home import home_page
from views.homepage import homepage
from views.data import data_page
from views.profile import profile_page


def main(page: ft.Page):
    # page.theme = ft.ThemeMode.DARK

    app_routes = [
        path(url="/", view=login_page, clear=True),
        path(url="/login", view=login_page, clear=True),
        path(url="/register", view=register_page, clear=True),
        path(url="/home/:user_id", view=homepage, clear=True),
        path(url="/data/:user_id", view=data_page, clear=True),
        path(url="/profile/:user_id", view=profile_page, clear=True)
    ]

    Routing(page=page, app_routes=app_routes)

    page.go(page.route)

    page.update()

    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(
    #         login_page(page),
    #     )
    #
    #     if page.route == "/home":
    #         page.views.append(
    #             homepage(page),
    #         )
    #
    #     if page.route == "/register":
    #         page.views.append(
    #             register_page(page),
    #         )
    #
    #     page.update()
    #
    # def view_pop():
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)
    #
    # page.on_route_change = route_change
    # page.on_view_pop = view_pop
    # page.go(page.route)

    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(login_page(page))
    #
    #     if page.route == "/home":
    #         page.views.append(home_page(page))
    #
    #     page.update()
    #
    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)
    #
    # page.on_route_change = route_change
    # page.on_view_pop = view_pop
    # page.go(page.route)


ft.app(target=main)
